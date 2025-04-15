# mapping.py

def map_stress_level(mood):
    stress_map = {
        "My brain's doing cartwheels and not in a good way.": 10,
        "I can't focus—everything's shiny and distracting!": 8,
        "I need energy... or a nap. Either works.": 5,
        "Anxious gremlins are on the loose again.": 7,
        "My head's thumping like a rave. Make it stop.": 9,
        "Feeling okay, just wanna level up my chill/focus.": 3
    }
    return stress_map.get(mood, 0)  # Default to 0 if mood not found

def map_adhd_symptoms(symptoms):
    # A simple mapping for ADHD symptoms
    adhd_symptoms = ["Attention span of a goldfish", "Can't sit still"]
    return any(symptom in adhd_symptoms for symptom in symptoms)

def map_migraine_frequency(symptoms):
    # A simple mapping for migraine frequency
    if "Migraines or regular headaches" in symptoms:
        return 5  # Example frequency
    return 0
