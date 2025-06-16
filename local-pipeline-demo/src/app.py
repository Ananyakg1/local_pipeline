from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))

# Sample quiz data
QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Madrid"],
        "answer": 2
    },
    {
        "id": 2,
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": 1
    },
    {
        "id": 3,
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "Mark Twain", "J.K. Rowling", "Jane Austen"],
        "answer": 0
    }
]

@app.route('/')
def home():
    return render_template('quiz.html')

@app.route('/api/questions')
def get_questions():
    # Don't send the answer index to the frontend
    questions = [
        {"id": q["id"], "question": q["question"], "options": q["options"]}
        for q in QUIZ_QUESTIONS
    ]
    return jsonify(questions)

@app.route('/api/submit', methods=['POST'])
def submit_quiz():
    data = request.json
    user_answers = data.get('answers', {})
    score = 0
    results = []
    for q in QUIZ_QUESTIONS:
        user_ans = user_answers.get(str(q["id"]))
        correct = (user_ans == q["answer"])
        results.append({
            "id": q["id"],
            "correct": correct,
            "correct_answer": q["options"][q["answer"]]
        })
        if correct:
            score += 1
    return jsonify({"score": score, "total": len(QUIZ_QUESTIONS), "results": results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
