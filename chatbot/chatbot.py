from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import pyttsx3
import webbrowser
mybot=ChatBot('Bot',logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                    'chatterbot.logic.BestMatch',
                                    'chatterbot.logic.TimeLogicAdapter'])
trainer=ListTrainer(mybot)
trainer.train([])
trainer=ChatterBotCorpusTrainer(mybot)
trainer.train('chatterbot.corpus.english','chatterbot.corpus.english.conversations')
def speak(command):
   text_speech=pyttsx3.init()
   text_speech.say(command)
   text_speech.runAndWait()
while True:
   qns=input('Me:')
   if qns=='bye':
      break
   elif 'search' in qns:
      print('searching....',qns.split('search')[1])
      url='https://www.youtube.com/search?q='+qns.split('search')[1]
      print(url)
      try:
         webbrowser.get().open(url)
         print('This is what i found')
      except:
         print('check your internet connection')
   else:     
      response=mybot.get_response(qns)
      print('Bot:',response)
      speak(response)