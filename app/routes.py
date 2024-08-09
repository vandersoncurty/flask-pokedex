from flask import Blueprint

# Cria um blueprint chamado 'main'
main = Blueprint('main', __name__)

@main.route('/')
def hello_world():
    return 'Hello, World!'
