from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    print hello_world



# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello, World'