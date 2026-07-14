import speech_recognition as sr

# Supported languages
LANGUAGE_CODES = {
    "English": "en-IN",
    "Hindi": "hi-IN",
    "Marathi": "mr-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Kannada": "kn-IN",
    "Malayalam": "ml-IN",
    "Gujarati": "gu-IN",
    "Punjabi": "pa-IN",
    "Bengali": "bn-IN",
    "Odia": "or-IN",
    "French": "fr-FR",
    "German": "de-DE",
    "Spanish": "es-ES",
    "Japanese": "ja-JP"
}


def recognize_speech(language):
    """
    Listen from microphone and convert speech to text.
    """

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            print("🎤 Listening...")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        text = recognizer.recognize_google(
            audio,
            language=LANGUAGE_CODES.get(language, "en-IN")
        )

        print("Recognized:", text)

        return text

    except sr.WaitTimeoutError:
        return "No speech detected."

    except sr.UnknownValueError:
        return "Could not understand."

    except sr.RequestError:
        return "Internet connection required."

    except Exception as e:
        return f"Error: {e}"