from flask import Flask, render_template, session, request, jsonify
app = Flask(__name__)
app.secret_key = 'your_secret_key'


# ROUTES
@app.route('/', methods=['GET', 'POST'])
def main():
    # Set initial score to 0 if it doesn't exist in session
    if 'score' not in session:
        session['score'] = 0
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
   return render_template('quiz.html')

@app.route('/quiz<int:id>', methods=['GET', 'POST'])
def quiz_id(id):
    # Constructs the filename based on the quiz ID
    quiz_file = f'quiz{id}.html'
    return render_template(quiz_file)

# Function to reset the score to 0
@app.route('/reset_score', methods=['POST'])
def reset_score():
    session['score'] = 0
    return jsonify({'message': 'Score reset successfully'})

# Function to add 1 point to the score
@app.route('/add_point', methods=['POST'])
def add_point():
    session['score'] += 1
    return jsonify({'message': 'Point added successfully'})

if __name__ == '__main__':
   app.run(debug=True)
