from telegram.ext import Updater, CommandHandler

def main():
    # Instaciamos el updater
    #updater = Updater(token=open("./bot_token").read(), use_context=True)
    updater = Updater(token="1037833024:AAEWhXnPqLuAM7cN71e_EUpZItgmeGnzTD0", use_context=True)
    #reparte el trabajo entre todos los manejadores. Añadimos manejador al comando /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # añadir manejador para el comando repite
    updater.dispatcher.add_handler(CommandHandler("repite",repite))

    # añadir suma
    updater.dispatcher.add_handler(CommandHandler("suma",suma))

    # Empezamos a pedir notificaciones a Telegram
    updater.start_polling()
    #Capturamos señales de parada
    updater.idle()


# definimos qué hace cuando ejecutamos /start
def start(update, context):
    update.message.reply_text("Hola, soy un bot")
    
# definimos qué hace cuando ejecutamos /repite

def repite(update, context):
    update.message.reply_text(update.message.text)

# definimos qué hace cuando ejecutamos /suma

def suma (update, context):
    # args = [2,2]
    resultado = int(context.args[0]) + int(context.args[1])
    update.message.reply_text("El resultado es " + str(resultado))

main()