"""
Sets the mapping between `url_endpoints` and `view functions`.
"""
from lib.utils import set_trace

routes = [
    # Define non-blueprint rotues here. Blueprint routes should be in
    # a separate urls.py inside the blueprint package.
]


def set_urls(app, routes=routes):
    """
    Connects url patterns to actions for the given wsgi `app`.
    """
    for rule in routes:
        # Set url rule.
        url_rule, endpoint, view_func, opts = parse_url_rule(rule)
        app.add_url_rule(url_rule, endpoint=endpoint, view_func=view_func, **opts)

def parse_url_rule(rule):
    """
    Breaks `rule` into `url`, `endpoint`, `view_func` and `opts`
    """
    length = len(rule)
    if length == 4:
        # No processing required.
        return rule
    elif length == 3:
        rule = list(rule)
        endpoint = None
        opts = {}
        if isinstance(rule[2], dict):
            # Options passed.
            opts = rule[2]
            view_func = rule[1]
        else:
            # Endpoint passed.
            endpoint = rule[1]
            view_func = rule[2]
        return (rule[0], endpoint, view_func, opts)
    elif length == 2:
        url_rule, view_func = rule
        return (url_rule, None, view_func, {})
    else:
        raise ValueError('URL rule format not proper %s' % (rule, ))
