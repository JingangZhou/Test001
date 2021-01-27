from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'.format(name)
    
@app.route('/<name>')
def index(name):
    return '<h1>Hello {}!</h1>'.format(name.capitalize())
    
    