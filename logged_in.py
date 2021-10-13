from flask import Flask, render_template, request, redirect
from flask.helpers import make_response, url_for
from functools import wraps

app = Flask(__name__)


def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if not request.cookies.get('authenticated'):
            return redirect(url_for('login'))

        return f(*args, **kws)
    return decorated_function


@app.route('/secret1')
@authorize
def secret1():
    return render_template("secret1.html")


@app.route('/secret2')
@authorize
def secret2():
    print("banan")
    return render_template("secret2.html")


@app.route('/delete')
@authorize
def delete_cookie():
    res = make_response(redirect(url_for('login')))
    res.set_cookie('authenticated', 'bar', max_age=0)
    return res


@app.route("/login", methods=['post', 'get'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        res = make_response(render_template('login.html'))
        if not request.cookies.get('authenticated'):
            res.set_cookie('authenticated', 'True')

        return res


@app.route('/')
def kek():
    return redirect(url_for('login'))


def start_flask():
    app.run()
