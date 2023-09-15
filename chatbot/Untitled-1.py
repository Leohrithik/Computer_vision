from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot=ChatBot('myBot')
trainer=ListTrainer(bot)
trainer.train(['I want to book movie tickets',
               'which movie are you looking for?',
               'what movies are playing now?',
               '1.2018 2.fast x',
               '2018',
               'for what day?',
               'today evening',
               'how many tickets are you looking for?',
               '3'
               ])
trainer.train(['1.2018 2.fast x',
               'fast x',
               'for what day?',
               'today evening',
               'how many tickets are you looking for?',
               '3'
               ])
while True:
   qns=input('Me:')
   if qns=='bye':
      print('Bye')
      break
   else:     
      res=bot.get_response(qns)
      print('Bot:',res)