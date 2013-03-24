
def run_server(app, port=8080):
    from tornado.wsgi import WSGIContainer
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop

    # Initialize app and serve.
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(port)
    IOLoop.instance().start()

if __name__ == '__main__':
    import main
    run_server(main.app)
