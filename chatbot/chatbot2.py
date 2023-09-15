from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot=ChatBot('myBot')
trainer=ListTrainer(bot)
trainer.train(['Hello'
               'hai'
               'how do you feel?'
               'im good'])
while True:
   qns=input('Me:')
   if qns=='bye':
      print('Bye')
      break
   else:     
      res=bot.get_response(qns)
      print('Bot:',res)