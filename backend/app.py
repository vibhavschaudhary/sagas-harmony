from flask import Flask, request, jsonify
from flask_cors import CORS
from logic.rules import get_recommendation  # Make sure logic/rules.py exists!
from logic.questionnaire import get_questionnaire
from logic.recommendation import get_recommendation, get_ml_recommendation
from logic.mapping import map_stress_level, map_adhd_symptoms, map_migraine_frequency

app = Flask(__name__)
CORS(app)

@app.route('/questionnaire', methods=['GET'])  # ← NEW endpoint
def questionnaires():
    return jsonify(get_questionnaire())

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()  # Fixed the indentation here
    # Extract responses from the questionnaire
    responses = data.get("responses", {})
    
    stress_level = map_stress_level(responses.get("mood"))
    adhd_symptoms = map_adhd_symptoms(responses.get("symptoms", []))
    migraine_frequency = map_migraine_frequency(responses.get("symptoms", []))

    recommendations = get_recommendation(stress_level, adhd_symptoms, migraine_frequency)

    return jsonify({
        "recommendations": recommendations
    })

if __name__ == '__main__':
    app.run(debug=True)
