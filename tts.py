from gtts import gTTS
import pygame
import os
import time

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

pygame.mixer.init()


def speak(text, language):

    if text.strip() == "":
        return

    filename = "voice.mp3"

    try:

        tts = gTTS(
            text=text,
            lang=LANGUAGE_CODES[language]
        )

        tts.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.unload()

        os.remove(filename)

    except Exception as e:
        print("Speech Error:", e)