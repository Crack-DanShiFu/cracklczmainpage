from . import auth
from .server import *


@auth.route('/login', methods=['POST'])
def login():
    pass
