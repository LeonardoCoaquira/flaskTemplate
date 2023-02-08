from flask import Flask, request
from markupsafe import escape
from flask import url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def get():
    return 'index'

@app.post('/')
def index():
    return 'post'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


if __name__ == '__main__':
    app.run(port=8080, debug=True, threaded=True)