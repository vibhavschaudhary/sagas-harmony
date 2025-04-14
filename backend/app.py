from flask import Flask, request, jsonify
from flask_cors import CORS
from logic.rules import get_recommendation # Make sure logic/rules.py exists!
app = Flask(__name__)
CORS(app)
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    symptoms = data.get("symptoms", [])
    result = get_recommendation(symptoms)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
