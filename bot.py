import telebot
from telebot import types
from pymongo import MongoClient
import os

client = MongoClient(os.environ["MongoDB"])
db = client.main
rulesColl = db.rules
adminsColl=db.admins


admins2=adminsColl.find_one({"ID": 2552})

bot=telebot.TeleBot(os.environ["TELEGRAM_TOKEN"])

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет! Подробно в /help")

@bot.message_handler(commands=['help'])
def start_message(message):
  bot.send_message(message.chat.id,"Команды:\n/rules - Правила чата.")

@bot.message_handler(commands=['infoc'])
def chatInfo(message):
  bot.send_message(message.chat.id,F"Айди чата: {message.chat.id}")

@bot.message_handler(commands=['infou'])
def userInfo(message):
	if message.reply_to_message!=None:
		bot.send_message(message.chat.id,f"Айди учатника: {message.reply_to_message.from_user.id}")

@bot.message_handler(commands=['infom'])
def chatInfo(message):
	if message.reply_to_message!=None:
		bot.send_message(message.chat.id,f"Айди сообщения: {message.reply_to_message.message_id}")
	
@bot.message_handler(commands=['rules'])
def rules(message):
	if message.chat.id==-1001317298639:
		rulesid=rulesColl.find_one({"rules": {'$exists': True}})
		rulesChatId=rulesColl.find_one({"chatid": {'$exists': True}})
		bot.forward_message(message.chat.id,f"{rulesChatId['chatid']}",f"{rulesid['rules']}")

@bot.message_handler(commands=['newrules'])
def newrules(message):
	if message.reply_to_message!=None:
		if message.from_user.id==f"{admins2['Tequila']}" or f"{admins2['AtikD']}":
			deleterules = rulesColl.delete_many ({})
			newrules = { "rules": message.reply_to_message.message_id,"chatid":message.chat.id}
			rulesColl.insert_one(newrules)
			bot.send_message(message.chat.id,"Правила установлены!")	    



''''
@bot.message_handler(commands=['gay'])
def start_message(message):
  bot.send_message("Гей чата будет "###):
@bot.message_handler(content_types=['text'])
def text_content(message):
	chatid=coll.find_one({'chatid':message.chat.id})
	if chatid==None:
		reg1 = { "chatid": message.chat.id,"ctrl":0 }
		coll.insert_one(reg)
  else:
    chatid=coll.find_one({'chatid':message.chat.id})
    if chatid!=None:
      for ids in chatid['users']:
        if chatid['users'][ids]['name'] == username1:
'''



bot.polling(none_stop=True)
