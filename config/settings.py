"""
Default settings supported by Flask. Additional keys can be put
in here which will be accessible in `app.config` dictionary like
object.
"""
import sys
import os
import logging
import importlib
from lib.middlewares import MethodRewriteMiddleware

from .blueprints import *

DEBUG = False
TESTING = False
#: Enable CSRF. Might not be needed if WTForms is used.
CSRF_ENABLED = True
#: Key for CSRF.
CSRF_SESSION_KEY = '\x126S{\x94\xbf}o5YE\xac\x17\x8e8^_\x18z\x08\xf3z1\x97'
#: Session signing key.
SECRET_KEY = '\x18[F;(\x99\xbcF\xc8\xe3\xb5\x89R\xb7[\x17H\x85\xd8\xa9,\xbf\x95\xb4;\xe1\x80\x872+\x82\x93'

#: Before request middlewares.
BEFORE_REQUESTS = [
]

#: After request middlewares.
AFTER_REQUESTS = []

#: Middlewares to enable.
#: Middlewares are executed in the order specified.
MIDDLEWARES = [
    #: Emulate RESTFul API for client that dont' directly
    #: support REST.
    # (middleware, *args, **kwargs)
    MethodRewriteMiddleware,
]

stream_logger = logging.StreamHandler()
stream_logger.setFormatter(logging.Formatter('''
                                             Message type:       %(levelname)s
                                             Location:           %(pathname)s:%(lineno)d
                                             Module:             %(module)s
                                             Function:           %(funcName)s
                                             Time:               %(asctime)s

                                             Message:

                                             %(message)s
                                             '''
                                            ))
stream_logger.setLevel(logging.DEBUG)

#: Custom log handlers.
LOG_HANDLERS = [stream_logger]

#: Jinja2 filters.
#TEMPLATE_FILTERS = [('custom_reverse', lambda x: x[::-1])]
TEMPLATE_FILTERS = []

#: Jinja2 context processors.
#CONTEXT_PROCESSORS = {name: val}
CONTEXT_PROCESSORS = {
}

#: Error handlers for http and other arbitrary exceptions.
#ERROR_HANDLERS = [(404, lambda error: ("Page not found", 404))]
ERROR_HANDLERS = []

HTTP_USERNAME = 'admin'
HTTP_PASSWORD = 'password'

# Load appropriate settings.
environ = os.environ.get('FLASK_ENV')
# Set environment specific settings.
if environ:
    _this_module = sys.modules[__name__]
    try:
        _m = importlib.import_module('config.%s_settings' % environ)
    except ImportError, ex:
        pass
    else:
        for _k in dir(_m):
            setattr(_this_module, _k, getattr(_m, _k))
# Dev is the default environment.
else:
    try:
        from dev_settings import *
    except ImportError, ex:
        pass
