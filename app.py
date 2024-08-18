from flask import Flask, render_template, request, redirect, url_for
from response import generate_questions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Get the number of questions from the form
    num_easy = int(request.form['easy'])
    num_medium = int(request.form['medium'])
    num_difficult = int(request.form['difficult'])

    # Generate questions using the function from response.py
    selected_questions = generate_questions(num_easy, num_medium, num_difficult)

    # Redirect to the response page with the generated questions
    return render_template('response.html', questions=selected_questions)

if __name__ == '__main__':
    app.run(debug=True)