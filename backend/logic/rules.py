def get_recommendation(symptoms):
    RULES = {
        "stress": ["binaural beats", "meditation music"],
        "ADHD": ["lofi focus tracks", "white noise"],
        "migraine": ["nature sounds", "soft ambient"],
        "anxiety": ["calm piano", "ocean waves"],
        "insomnia": ["sleep sounds", "delta waves"]
    }

    recommendations = set()

    for symptom in symptoms:
        therapies = RULES.get(symptom.lower())
        if therapies:
            recommendations.update(therapies)

    return {
        "therapy": list(recommendations) or ["default ambient music"],
        "note": "Rule-based recommendation"
    }
