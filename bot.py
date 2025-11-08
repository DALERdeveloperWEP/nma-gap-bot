from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import Config
from callbacks import start, send_orders, send_about


def main() -> None:
    updater = Updater(Config.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        handler=CommandHandler(
            command='start',
            callback=start
        )
    )

    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('📦 Buyurtmalarim'),
            callback=send_orders
        )
    )
    
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('ℹ️ Biz haqimizda'),
            callback=send_about
        )
    )

    updater.start_polling()
    updater.idle()

main()
