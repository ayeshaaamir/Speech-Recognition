#speech to text
import speech_recognition as sr
record=sr.Recognizer()
with sr.Microphone() as source:
  record.adjust_for_ambient_noise(source)
  print("speak....")
  audio=record.listen(source)

try:
  print("text: " + recording.recognize_google(audio))
except Exception as e:
  print(e)

