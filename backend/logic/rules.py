def get_recommendation(symptoms):
    # Simple rule-based system
    recommendations = []

    if "stress" in symptoms:
        recommendations.append("binaural beats")
    if "ADHD" in symptoms:
        recommendations.append("lofi focus tracks")
    if "migraine" in symptoms:
        recommendations.append("nature sounds")

    return {
        "therapy": recommendations or ["default ambient music"],
        "note": "Rule-based recommendation"
    }
