# vim: set fileencoding=utf-8 :
"""
Misc. utilities.
"""
def set_trace():
    """
    Wrapper for ``pdb.set_trace``.
    """
    from config import app
    if not app.debug: return
    import pdb
    pdb.set_trace()

def simple_form(form_type, template, success):
    from flask import render_template
    def fn():
        form = form_type()
        if form.validate_on_submit():
            return success()
        return render_template(template, form=form)
    return fn

def http_auth(username, password, include, *endpoints):
    from flask import request, Response
    def protected():
        if request and request.endpoint and not request.endpoint.startswith('_'):
            if include:
                predicate = request.endpoint in endpoints
            else:
                predicate = request.endpoint not in endpoints
            if predicate:
                auth = request.authorization
                if not auth or not (auth.username == username and auth.password == password):
                    return Response('Could not verify your access level for that URL.\n'
                                    'You have to login with proper credentials', 401,
                                    {'WWW-Authenticate': 'Basic realm="Login Required"'})
    return protected

def http_do_auth(username, password, *endpoints):
    return http_auth(username, password, True, *endpoints)

def http_dont_auth(username, password, *endpoints):
    return http_auth(username, password, False, *endpoints)

def row_to_dict(row):
    return dict((col, getattr(row, col)) for col in row.__table__.columns.keys())

def rows_to_dict(rows):
    return map(row_to_dict, rows)
