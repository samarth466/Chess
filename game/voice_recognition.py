import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound

def speak(text,lang):
    tts = gTTS(text=text,lang=lang)
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)