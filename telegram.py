import telebot
from telebot import types
import os
import random

token = 'token'
bot = telebot.TeleBot(token)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = types.KeyboardButton("Старт")
    action_button = types.KeyboardButton("Фото Бони")
    markup.add(start_button, action_button)
    bot.send_message(message.chat.id, 
                    text=f"Привет, {message.from_user.first_name}\nВоспользуйся кнопками", 
                    reply_markup=markup)

# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def buttons(message):
    if message.text == "Старт":
        bot.send_message(message.chat.id, "Я могу отправлять фото, нажми на кнопку 'Фото Бони'")
    elif message.text.lower() == "фото бони":
        photo_dir = r'C:\Users\user\Desktop\bonya_bot\photos'
        try:
            photos = [f for f in os.listdir(photo_dir) 
                     if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            
            if not photos:
                bot.send_message(message.chat.id, "В папке нет изображений")
                return
                
            photo_name = random.choice(photos)
            photo_path = os.path.join(photo_dir, photo_name)
            
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        except Exception as e:
            bot.send_message(message.chat.id, f"Произошла ошибка: {e}")
    else:
        bot.send_message(message.chat.id, "Я могу отвечать только на нажатие кнопок")

# Запуск бота
bot.polling(none_stop=True)
