import telebot
from news import (
    news_apple_sfera,
    news_fayer,
    news_goole,
    news_muylinux,
    news_xataka,
    news_xataka_android,
)

bot = telebot.TeleBot("6493247672:AAELFqWHbi2EbYKvrrRc6Wg-N_U8-9YaC4w")

# Funciones para obtener noticias
def get_applesfera_news(message):
    print('Apple Esfera - Principales noticias Sr Yonier')
    print('='*130)
    for new in news_apple_sfera.news('https://www.applesfera.com/'):
        bot.send_message(message.chat.id, new)

def get_fayer_news(message):
    print('Fayer Wayer - Principales noticias Sr Yonier')
    print('='*130)
    for new in news_fayer.news('https://www.fayerwayer.com/internet/', 'https://www.fayerwayer.com'):
        bot.send_message(message.chat.id, new)

def get_google_news(message):
    print('Google - Principales noticias Sr Yonier')
    print('='*130)
    for new in news_goole.news('https://news.google.com/topics/CAAqLQgKIidDQkFTRndvSkwyMHZNR1ptZHpWbUVnWmxjeTAwTVRrYUFrTlBLQUFQAQ?hl=es-419&gl=CO&ceid=CO%3Aes-419', 'https://news.google.com/topics'):
        bot.send_message(message.chat.id, new)

def get_xataka_news(message):
    print('Xataka - Principales noticias Sr Yonier')
    print('='*130)
    for new in news_xataka.news('https://www.xataka.com/'):
        bot.send_message(message.chat.id, new)

# Diccionario que mapea comandos a funciones
command_functions = {
    '/applesfera': get_applesfera_news,
    '/fayer': get_fayer_news,
    '/google': get_google_news,
    '/xataka': get_xataka_news,
}

@bot.message_handler(commands=['applesfera', 'fayer', 'google', 'xataka' ])
def handle_commands(message):
    command = message.text
    if command in command_functions:
        command_functions[command](message)
    else:
        bot.send_message(message.chat.id, 'Comando no válido')

@bot.message_handler(content_types=['text'])
def no_found_command(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, 'Comando no disponible')
    else:
        bot.send_message(message.chat.id, 'Los comandos disponibles son /xataka /xatakandroid')

if __name__ == '__main__':
    print('='*100)
    print('Iniciando Bot')
    print('='*100)
    bot.infinity_polling()

