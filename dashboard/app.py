from flask import Flask, render_template, request, jsonify

# Create the Flask app
app = Flask(__name__)


# Define the route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for the phases, log and settings
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
