import telebot
from news import news_apple_sfera, news_fayer, news_goole, news_muylinux, news_xataka, news_xataka_android


bot = telebot.TeleBot("6493247672:AAELFqWHbi2EbYKvrrRc6Wg-N_U8-9YaC4w")


@bot.message_handler(commands=['applesfera', 'fayer', 'google', 'xataka', 'google' ])
def get_new(message):
    """Noticias de tecnologia"""
    if message.text.startswith("/applesfera"):
        print('Apple Esfera - Principales noticias Sr Yonier')
        print('='*130)
        for new in news_apple_sfera.news('https://www.applesfera.com/'): 
            bot.send_message(message.chat.id, new )
            
    elif message.text.startswith("/fayer"):
        print('Fayer Wayer - Principales noticias Sr Yonier')
        print('='*130)
        for new in news_fayer.news('https://www.fayerwayer.com/internet/', 'https://www.fayerwayer.com'): 
            bot.send_message(message.chat.id, new )
        
    elif message.text.startswith("/google"):
        print('Google - Principales noticias Sr Yonier')
        print('='*130)
        for new in news_goole.news('https://news.google.com/topics/CAAqLQgKIidDQkFTRndvSkwyMHZNR1ptZHpWbUVnWmxjeTAwTVRrYUFrTlBLQUFQAQ?hl=es-419&gl=CO&ceid=CO%3Aes-419', 'https://news.google.com/topics'): 
            bot.send_message(message.chat.id, new )
    
    elif message.text.startswith("/xataka"):
        print('Xataka - Principales noticias Sr Yonier')
        print('='*130)
        for new in news_xataka.news('https://www.xataka.com/'): 
            bot.send_message(message.chat.id, new )
            

            
    else:
        bot.send_message(message.chat.id, 'Comando /xataka')
    

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
