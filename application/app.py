from flask import Flask, render_template
from os import environ

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

API_KEY = environ.get('API_KEY')
app.secret_key = environ.get('SECRET_KEY')
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024


# App Starting
@app.route('/')
def index():
    return "Flask - Nginx - Docker"


if __name__ == '__main__':
    app.run()
