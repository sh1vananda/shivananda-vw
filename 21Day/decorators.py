from functools import wraps
from flask import session
 
def role_required(roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if "role" not in session:
                return "Access Denied"
            if session["role"] not in roles:
                return "Access Denied"
            return f(*args, **kwargs)
        return wrapper
    return decorator
 
 
