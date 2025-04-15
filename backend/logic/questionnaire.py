def get_questionnaire():
    return {
        "title": "Discover Your Harmony Vibe",
        "questions": [
            {
                "id": "mood",
                "text": "Pick a vibe that best matches your current mood:",
                "type": "single",
                "options": [
                    "My brain's doing cartwheels and not in a good way.",
                    "I can't focus—everything's shiny and distracting!",
                    "I need energy... or a nap. Either works.",
                    "Anxious gremlins are on the loose again.",
                    "My head's thumping like a rave. Make it stop.",
                    "Feeling okay, just wanna level up my chill/focus."
                ]
            },
            {
                "id": "symptoms",
                "text": "What's been following you around like a clingy Spotify ad lately?",
                "type": "multiple",
                "options": [
                    "Work or study stress",
                    "Attention span of a goldfish",
                    "Migraines or regular headaches",
                    "Trouble winding down or sleeping",
                    "Anxiety lurking in the background",
                    "Honestly, I'm vibin'"
                ]
            },
            {
                "id": "sound_pref",
                "text": "What's your sound sanctuary?",
                "type": "multiple",
                "options": [
                    "Gentle rain or forest whispers",
                    "Soothing ambient waves",
                    "Deep-focus binaural beats",
                    "Chill lo-fi beats to study/cry to",
                    "Elegant classical instrumentals",
                    "White noise to block out reality",
                    "Surprise me, maestro"
                ]
            },
            {
                "id": "lifestage",
                "text": "What's your stage of life right now?",
                "type": "single",
                "options": [
                    "Buried in books (Student life)",
                    "Grinding 9 to 5 (Working life)",
                    "Home is where the heart (and chaos) is",
                    "Living life unplugged (Retired / Taking it slow)",
                    "Somewhere between it all"
                ]
            },
            {
                "id": "age_group",
                "text": "Age group (for tuning the experience just right):",
                "type": "single",
                "options": [
                    "Under 18",
                    "18-25",
                    "26-35",
                    "36-50",
                    "50+"
                ]
            }
        ]
    }
