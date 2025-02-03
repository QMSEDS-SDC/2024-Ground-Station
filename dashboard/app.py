from flask import Flask, render_template, request, jsonify

# Init
app = Flask(__name__)


# Routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/phase1')
def phase1():
    return render_template('phase1.html')


@app.route('/phase2')
def phase2():
    return render_template('phase2.html')


@app.route('/phase3')
def phase3():
    return render_template('phase3.html')


@app.route('/log')
def log():
    return render_template('log.html')


@app.route('/config')
def settings():
    return render_template('config.html')
