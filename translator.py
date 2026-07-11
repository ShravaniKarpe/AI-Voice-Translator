from deep_translator import GoogleTranslator

language_codes = {
    "English": "en",
    "Marathi": "mr",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te"
}

def translate_text(text, source, target):
    translated = GoogleTranslator(
        source=language_codes[source],
        target=language_codes[target]
    ).translate(text)

    return translated