from flask import (Flask, render_template, request, redirect, jsonify, url_for,
                   flash)
from flask import session as login_session

app = Flask(__name__)


@app.route('/')
def home():
    return "home page here"

if __name__ == '__main__':
    app.secret_key = 'super_secret_key1'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
