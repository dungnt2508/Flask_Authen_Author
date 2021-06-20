from flask import Blueprint

bp = Blueprint('bp', __name__)

from . import auth
from . import main




