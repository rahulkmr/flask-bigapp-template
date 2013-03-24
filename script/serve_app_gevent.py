from gevent.monkey import patch_all
patch_all()

def run_server(app, port=8080):
    from gevent.pywsgi import WSGIServer
    http_server = WSGIServer(('', port), app)
    http_server.serve_forever()

if __name__ == '__main__':
    import main
    run_server(main.app)
