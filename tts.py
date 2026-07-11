from gtts import gTTS
import pygame
import os
import time

language_codes = {
    "English":"en",
    "Marathi":"mr",
    "Hindi":"hi",
    "Tamil":"ta",
    "Telugu":"te"
}

def speak(text, language):

    filename = "output.mp3"

    gTTS(
        text=text,
        lang=language_codes[language]
    ).save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.quit()

    os.remove(filename)