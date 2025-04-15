# logic/recommendation.py

def get_recommendation(stress_level, adhd_symptoms, migraine_frequency):
    # Rule-based logic
    recommendations = []
    
    # Rule 1: If stress is high, recommend stress management
    if stress_level > 7:
        recommendations.append("Stress Relief Therapy")
        
    # Rule 2: If ADHD symptoms are present, recommend focus exercises
    if adhd_symptoms:
        recommendations.append("Focus Therapy")

    # Rule 3: If migraine frequency is high, recommend migraine management
    if migraine_frequency > 3:
        recommendations.append("Migraine Relief Therapy")

    # Combine the results and return
    return recommendations


def get_ml_recommendation(stress_level, adhd_symptoms, migraine_frequency):
    # Placeholder function for ML-based recommendation (using trained model)
    # This would integrate with your trained ML model (e.g., TensorFlow, Scikit-learn)
    # For now, it's a dummy placeholder.
    
    # Assuming the model predicts a therapy plan based on input
    if stress_level > 7 and adhd_symptoms and migraine_frequency > 3:
        return ["Stress Relief Therapy", "Focus Therapy", "Migraine Relief Therapy"]
    else:
        return ["General Wellness"]
