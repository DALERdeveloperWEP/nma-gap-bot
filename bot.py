from telegram.ext import Updater, CommandHandler

from config import Config
from callbacks import start


def main() -> None:
    updater = Updater(Config.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        handler=CommandHandler(
            command='start',
            callback=start
        )
    )

    updater.start_polling()
    updater.idle()

main()
