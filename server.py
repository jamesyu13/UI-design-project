from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

import logging

# ROUTES
@app.route('/')
def home():
    return render_template('home.html')

# Beat and Tempo page route
@app.route('/beat-and-tempo')
def beat_and_tempo():
    return render_template('beat-and-tempo.html')

# Duration and Symbols page route
@app.route('/duration-and-symbols')
def duration_and_symbols():
    return render_template('duration-and-symbols.html')

# Subdividing page route
@app.route('/subdividing')
def subdividing():
    return render_template('subdividing.html')

# Quiz page route
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

if __name__ == '__main__':
   app.run(debug = True)