from flask import jsonify, request
from functools import wraps
from my_app.user.models import User

def check_auth(username, password, page =1):
    users = User.query.paginate(page, 10).items
    for user in users:
        if username == str(user.name):
            return password == str(user.password)
    return False

def authenticate():
    message = {'message': "Authenticate."}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'

    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth: 
            return authenticate()

        elif not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated