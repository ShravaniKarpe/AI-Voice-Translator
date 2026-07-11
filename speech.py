import speech_recognition as sr

language_codes = {
    "English": "en-IN",
    "Marathi": "mr-IN",
    "Hindi": "hi-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN"
}

def recognize_speech(language):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening... Speak now!")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )
        except sr.WaitTimeoutError:
            return "No speech detected."

    try:
        text = recognizer.recognize_google(
            audio,
            language=language_codes[language]
        )
        return text

    except sr.UnknownValueError:
        return "Could not understand speech."

    except Exception as e:
        return f"Error: {e}"