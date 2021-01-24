from telegram import Update
from telegram.ext import Updater, MessageHandler, CallbackContext, Filters, CommandHandler

from itertools import zip_longest

def pat(update: Update, context: CallbackContext) -> None:
    if "times_patted" not in context.chat_data:
        context.chat_data["times_patted"] = 0
    context.chat_data["times_patted"] += 1
    times_patted = context.chat_data["times_patted"]
    update.message.reply_text(f"This dog has been patted {times_patted} times")

updater = Updater('TOKEN')
updater.dispatcher.add_handler(CommandHandler("pat", pat))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    updater.start_polling()
    updater.idle()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
