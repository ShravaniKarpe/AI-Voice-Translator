from deep_translator import GoogleTranslator

# Language codes for translation
LANGUAGE_CODES = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Bengali": "bn",
    "Odia": "or",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja"
}


def translate_text(text, source_language, target_language):
    """
    Translate text between selected languages.
    """

    if not text:
        return ""

    try:
        translated = GoogleTranslator(
            source=LANGUAGE_CODES[source_language],
            target=LANGUAGE_CODES[target_language]
        ).translate(text)

        return translated

    except Exception as e:
        return f"Translation Error: {e}"