from flask import Blueprint

bp = Blueprint('auth', __name__)

from .routes import init_auth_routes
init_auth_routes(bp)
