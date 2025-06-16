from flask import Flask, render_template, jsonify
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/api/message')
def api_message():
    return jsonify({"message": "Hello from the backend API!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
