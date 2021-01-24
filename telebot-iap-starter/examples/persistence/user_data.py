from telegram import Update
from telegram.ext import Updater, MessageHandler, CallbackContext, Filters, CommandHandler, PicklePersistence

def new_item(update: Update, context: CallbackContext) -> None:
    if "entries" not in context.user_data:
        context.user_data["entries"] = list()
    context.user_data["entries"].append(" ".join(context.args))
    print(context.user_data["entries"])
    num_items = len(context.user_data["entries"])
    update.message.reply_text(f"Item added! You now have {num_items} items in your shopping list")


def list_items(update: Update, context: CallbackContext) -> None:
    if "entries" not in context.user_data:
        context.user_data["entries"] = list()
    num_items = len(context.user_data["entries"])
    shopping_list = "\n".join([f"- {item}" for item in context.user_data["entries"]])
    print(shopping_list)
    update.message.reply_text(f"You have {num_items} items in your shopping list: \n\n{shopping_list}")

# Create persistence by saving in a file
persistence = PicklePersistence("memory.pickle")

updater = Updater('TOKEN', persistence=persistence)

updater.dispatcher.add_handler(CommandHandler("add", new_item))
updater.dispatcher.add_handler(CommandHandler("list", list_items))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    updater.start_polling()
    updater.idle()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
