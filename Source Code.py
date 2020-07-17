import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile('ayeshacourses.wav') as source:
    audio_text = r.listen(source)
    try:
        text = r.recognize_google(audio_text)
        print('Converting audio into text')
        print(text)
    except:
         print('Sorry please try again')
