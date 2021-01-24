from telegram import Update
from telegram.ext import Updater, MessageHandler, CallbackContext, Filters, CommandHandler, PicklePersistence
from random import choice

def put(update: Update, context: CallbackContext) -> None:
    if "items" not in context.bot_data:
        context.bot_data["items"] = list()
    if not context.args:
        update.message.reply_text(f"You have to put something into the box")
        return
    if not " ".join(context.args).isalpha():
        update.message.reply_text(f"That is not a valid item")
        return
    item = ( update.message.from_user.id,
             update.message.from_user.first_name,
             " ".join(context.args)
             )
    context.bot_data["items"].append(item)
    print(context.bot_data["items"])
    update.message.reply_text(f" {''.join(context.args)} has been placed in the box")

def take(update: Update, context: CallbackContext) -> None:
    if "items" not in context.bot_data:
        context.bot_data["items"] = list()
    recipient_user_id = update.message.from_user.id
    # copies the items in the dictionary and stores in a list
    # add this line so that you cannot take your own gift: if gift[0] != recipient_user_id
    gifts = [gift for gift in context.bot_data["items"] ]
    # same as if len(gifts) == 0
    if not gifts:
        update.message.reply_text(f"There is nothing in the box")
        return
    randItem = choice(gifts)
    update.message.reply_text(f"You got a {randItem[2]} from {randItem[1]}")
    context.bot_data["items"].remove(randItem)

def list(update: Update, context: CallbackContext) -> None:
    if "items" not in context.bot_data:
        context.bot_data["items"] = list()
    numOfItems = len(context.bot_data["items"])
    mysteryBox = "\n".join([f"- {item[2]}" for item in context.bot_data["items"]])
    print(mysteryBox)
    update.message.reply_text(f"There are {numOfItems} items left in the mystery Box: \n{mysteryBox}")

persistence = PicklePersistence("memory.pickle")
updater = Updater('TOKEN', persistence=persistence)

updater.dispatcher.add_handler(CommandHandler("put", put))
updater.dispatcher.add_handler(CommandHandler("take", take))
updater.dispatcher.add_handler(CommandHandler("list", list))

if __name__ == '__main__':
    updater.start_polling()
    updater.idle()
