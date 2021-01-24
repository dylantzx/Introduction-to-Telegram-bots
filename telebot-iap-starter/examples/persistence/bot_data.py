from telegram import Update
from telegram.ext import Updater, MessageHandler, CallbackContext, Filters, CommandHandler

def greet(update: Update, context: CallbackContext) -> None:
    # user.id used to identify different users
    user_id = update.message.from_user.id
    # initialize for first time talking to bot
    if "users_talked_to" not in context.bot_data:
        # a set is a list that cannot contain duplicate elements
        context.bot_data["users_talked_to"] = set()
    context.bot_data["users_talked_to"].add(user_id)
    num_people = len(context.bot_data["users_talked_to"])
    update.message.reply_text(f"Hello! A total of {num_people} people have spoken to this bot.")


updater = Updater('TOKEN')

updater.dispatcher.add_handler(MessageHandler(Filters.text & (~ Filters.forwarded), greet))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    updater.start_polling()
    updater.idle()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
