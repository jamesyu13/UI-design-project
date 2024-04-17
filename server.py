from flask import Flask, render_template, session, request, jsonify
app = Flask(__name__)
app.secret_key = 'your_secret_key'


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
@app.route('/', methods=['GET', 'POST'])
def main():
    # Set initial score to 0 if it doesn't exist in session
    if 'score' not in session:
        session['score'] = 0
    return render_template('quiz.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    return render_template('quiz.html')


if __name__ == '__main__':
   app.run(debug=True)
