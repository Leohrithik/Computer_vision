import pyttsx3
text_speech=pyttsx3.init()
text=input('What you want to convert?\n')
text_speech.say(text)
text_speech.runAndWait()