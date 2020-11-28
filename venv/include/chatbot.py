from telebot import *
import os
token = "1428942350:AAHBheBhC2oBPXNGLAAaDEwF8j3XjrwL1J4"
bot = TeleBot(token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start','/stop')
    user_markup.row('Документ(условия участия)')
    bot.send_message(message.chat.id,"Тебя приветствует бот созданный командой Ab.ai! Для того, чтобы стать участником раздачи ноутбуков ты должен выбрать команду «Документ (условия участия)». В документе описаны все необходимые шаги которые нужно выполнить для участия. В случае если вы пройдёте в следующий этап, команда организует с вами онлайн интервью для уточнения всех деталей.", reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    user_markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,"Поздравляем! Скоро с вами свяжемся!",reply_markup=user_markup)

@bot.message_handler(content_types=["text"])
def messange_handler(message):
        if message.text == "hello":
            bot.send_message(message.chat.id, "Hello my friend")
        elif message.text == "Документ(условия участия)":
            directory = "/Users/gauhar/Desktop/giveaway"
            list_files = os.listdir(directory)
            for file_name in list_files:
                file = open(directory + "/" + file_name, "rb")
                bot.send_document(message.chat.id, file)
                file.close()
        else:
            bot.send_message(message.chat.id, "Ошибка! Следуйте правилам!")

def create_zip(path, zipfile):
    files = os.listdir(path)
    for file in files:
        if file != '.DS_Store':
            zipfile.write(file)

bot.polling(none_stop=True, interval=0)

