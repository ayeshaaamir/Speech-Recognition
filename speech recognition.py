#speech to text
import speech_recognition as sr
record=sr.Recognizer()
with sr.Microphone() as source:
  record.adjust_ambient_noise(source)
  
