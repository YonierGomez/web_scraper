import telebot
import news_fayer

bot = telebot.TeleBot("6493247672:AAELFqWHbi2EbYKvrrRc6Wg-N_U8-9YaC4w")


# Decorador, un decorador en python es una función que recibe parametros de otras funciones y retorna resultados, esto se usa para re-usar el código
@bot.message_handler(commands=["start", "help", "ayuda", 'noticias'])
def enviar(message):
    """Envia noticias"""
    noticias = news_fayer.news('https://www.fayerwayer.com/internet/', 'https://www.fayerwayer.com')

    if noticias:
        # Si hay noticias, envía cada una de ellas por separado
        for noticia in noticias:
            bot.reply_to(message, noticia)
    else:
        bot.reply_to(message, "No hay noticias disponibles en este momento.")

if __name__ == '__main__':
    print('='*100)
    print('Iniciando Bot')
    print('='*100)
    bot.infinity_polling() #mantiene al bot en modo escucha
