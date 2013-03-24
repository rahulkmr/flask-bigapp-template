"""
General purpose decorators and other utilities for contract based programming, for the
flask web framework.
"""
import re, sys, types
from functools import wraps
from collections import defaultdict

from flask import request

class AugmentError(ValueError):
    """
    Default exception raised when a contraint is voilated.
    """
    def __init__(self, errors):
        super(ValueError, self).__init__()
        self.errors = errors

    def __str__(self):
        """
        Dumps the `self.errors` dictionary.
        """
        return repr(self.errors)

def ensure_args(storage=None, error_handler=None, check_blank=True, **rules):
    """
    Ensures the value of `arg_name` satisfies `constraint`
    where `rules` is a collection of `arg_name=constraint`.
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            handler = error_handler or _get_error_handler(fn)
            errors = check_args(storage, check_blank, **rules)
            if errors:
                num_errors = len(errors)
                plural = 'errors' if num_errors > 1 else 'error'
                errors['base'].append('%s %s' % (num_errors, plural))
                return _propogate_error(errors, handler)
            else:
                return fn(*args, **kwargs)
        return wrapper
    return decorator

def ensure_presence(storage=None, error_handler=None, **args):
    arg_dict = {}
    for arg_name in args:
        arg_dict[arg_name] = (lambda x: x, '%s is required.' % arg_name)
    return ensure_args(storage=storage, error_handler=error_handler, **arg_dict)

def ensure_one_of(storage=None, error_handler=None, exclusive=False, check_blank=True, **rules):
    """
    `rules` is a dictionary of `arg_name=1` pairs.
    Ensures at least(or at most depending on `exclusive)` one of `arg_name`
    is passed and not null.
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            handler = error_handler or _get_error_handler(fn)
            errors = check_args(storage, check_blank, **rules)
            if errors:
                valid_count = len(rules) - len(errors)
                if valid_count < 1:
                    errors['base'].append('One of constraints must validate.')
                    return _propogate_error(errors, handler)
                elif valid_count > 1 and exclusive:
                    errors['base'].append('Only one of constraints should validate.')
                    return _propogate_error(errors, handler)
                else:
                    return fn(*args, **kwargs)
            else:
                if exclusive:
                    errors['base'].append('Only one of constraints should validate.')
                    return _propogate_error(errors, handler)
                else:
                    return fn(*args, **kwargs)
        return wrapper
    return decorator

def check_args(storage=None, check_blank=True, **rules):
    """
    Checks that `arg_val` satisfies `constraint` where `rules` is a
    dicionary of `arg_name=constraint` and `arg_val` is in `kwargs` or `args`
    """
    storage = storage or request.args
    results = []
    for arg_name, constraint in rules.iteritems():
        # Get the argument value.
        arg_val = storage.get(arg_name)
        if check_blank or arg_val:
            message = None
            if isinstance(constraint, list) or isinstance(constraint, tuple):
                if len(constraint) == 2:
                    constraint, message = constraint
                else:
                    raise ValueError('Constraints can either be "(constraint, message)" or "constraint"'
                                    '"%s" is in inproper format' % constraint)
            # `constraint` can either be a regex or a callable.
            validator = constraint
            if not callable(constraint):
                validator = lambda val: re.match(constraint, str(val))
            if message:
                results.append((arg_name, arg_val, validator(arg_val), message))
            else:
                results.append((arg_name, arg_val, validator(arg_val)))
    return _construct_errors(results, rules)

def _construct_errors(results, rules):
    """
    Constructs errors dictionary from the returned results.
    """
    errors = defaultdict(list)
    for res in results:
        message = None
        if len(res) == 4:
            arg_name, arg_val, valid, message = res
        else:
            arg_name, arg_val, valid = res
        if not valid:
            if not message:
                # No user supplied message. Construct a generic message.
                message = '"%s" violates constraint.' % arg_val
            errors[arg_name].append(message)
    return errors

def _propogate_error(errors, handler=None, exception_type=AugmentError):
    """
    Passes the errors to the handler or raises an exception.
    """
    if handler:
        return handler(errors)
    else:
        raise exception_type(errors)

def _get_error_handler(fn):
    error_handler = None
    if getattr(fn, '__name__', None):
        handler_name = '_%s_handler' % fn.__name__
        if isinstance(fn, types.FunctionType):
            mod = sys.modules[fn.__module__]
            error_handler = getattr(mod, handler_name, None)
        elif isinstance(fn, types.MethodType):
            error_handler = getattr(fn.im_class, handler_name, None)
    return error_handler


if __name__ == '__main__':
    import doctest
    doctest.testmod()
