import telebot

# Your Telegram Bot Token (Hardcoded for now)
bot = telebot.TeleBot('8045125371:AAHyV8-uE9QL6MCPy1pQv_l8rkU2OM90lEU')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Welcome! You'll start receiving trading signals shortly.")

def run_bot():
    bot.polling()