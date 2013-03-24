from werkzeug import url_decode

class MethodRewriteMiddleware(object):
    """
    Middleware to handle RESTful requests from clients which
    don't support whole of REST (GET, PUT, POST, DELETE).

    The method name is passed as a form field and the request
    is re-written here.
    """

    def __init__(self, app, input_name='_method'):
        self.app = app
        self.input_name = input_name

    def __call__(self, environ, start_response):
        if self.input_name in environ.get('QUERY_STRING', ''):
            args = url_decode(environ['QUERY_STRING'])
            method = args.get(self.input_name).upper()
            if method and method in ['GET', 'POST', 'PUT', 'DELETE']:
                method = method.encode('ascii', 'replace')
                environ['REQUEST_METHOD'] = method
        return self.app(environ, start_response)
