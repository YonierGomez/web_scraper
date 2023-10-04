import telebot, threading
from news import (
    news_apple_sfera,
    news_fayer,
    news_goole,
    news_muylinux,
    news_xataka,
    news_xataka_android,
    config
)

bot = telebot.TeleBot(config.VAR_TOKEN)

var_msj_news = 'Principales noticias Sr Yonier'
# Funciones para obtener noticias
def get_applesfera_news(message):
    print('Apple Esfera -', var_msj_news)
    print('='*130)
    for new in news_apple_sfera.news('https://www.applesfera.com/'):
        bot.send_message(message.chat.id, new)

def get_fayer_news(message):
    print('Fayer Wayer -', var_msj_news)
    print('='*130)
    for new in news_fayer.news('https://www.fayerwayer.com/internet/', 'https://www.fayerwayer.com'):
        bot.send_message(message.chat.id, new)

def get_muylinux_news(message):
    print('Muy Linux -', var_msj_news)
    print('='*130)
    for new in news_muylinux.news('https://www.muylinux.com/'):
        bot.send_message(message.chat.id, new)

def get_google_news(message):
    print('Google -', var_msj_news)
    print('='*130)
    for new in news_goole.news('https://news.google.com/topics/CAAqLQgKIidDQkFTRndvSkwyMHZNR1ptZHpWbUVnWmxjeTAwTVRrYUFrTlBLQUFQAQ?hl=es-419&gl=CO&ceid=CO%3Aes-419', 'https://news.google.com/topics'):
        bot.send_message(message.chat.id, new)

def get_xatakandroid_news(message):
    print('Xataka Android -', var_msj_news)
    print('='*130)
    for new in news_xataka.news('https://www.xatakandroid.com/'):
        bot.send_message(message.chat.id, new)

def get_xataka_news(message):
    print('Xataka -', var_msj_news)
    print('='*130)
    for new in news_xataka.news('https://www.xataka.com/'):
        bot.send_message(message.chat.id, new)

# Diccionario que mapea comandos a funciones
command_functions = {
    '/applesfera': get_applesfera_news,
    '/fayer': get_fayer_news,
    '/google': get_google_news,
    '/muylinux': get_muylinux_news,
    '/xatakandroid': get_xatakandroid_news,
    '/xataka': get_xataka_news,
}

comandos_sin_slash = [comando[1:] for comando in command_functions.keys()]

@bot.message_handler(commands=comandos_sin_slash)
def handle_commands(message):
    command = message.text
    if command in command_functions:
        command_functions[command](message)
    else:
        bot.send_message(message.chat.id, 'Comando no válido')

@bot.message_handler(content_types=['text'])
def no_found_command(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, f'Comando {message.text} no disponible')
    else:
        list_command =  f"Los comandos disponibles son {', '.join(command_functions.keys())}"
        bot.send_message(message.chat.id, list_command )


def listen():
    """Bucle infinito"""
    bot.infinity_polling() #ESCUCHA O COMPRUEBA SI SE RECIBEN MSJ NUEVOS, TODO SE DETIENE AQUI, 
    

if __name__ == '__main__':
    bot.set_my_commands([
        telebot.types.BotCommand("/applesfera", "muestra noticias de Apple"),
        telebot.types.BotCommand("/fayer", "muestra noticias sobre Fayer Wayer"),
        telebot.types.BotCommand("/google", "muestra noticias - Google News"),
        telebot.types.BotCommand("/muylinux", "muestra noticias sobre GNU/Linux"),
        telebot.types.BotCommand("/xatakandorid", "muestra noticias sobre Android"),
        telebot.types.BotCommand("/xataka", "muestra noticias - Xataka"),
    ])
    print('='*100)
    print('Iniciando Bot')
    print('='*100)
    hilo_bot = threading.Thread(target=listen)
    hilo_bot.start()
