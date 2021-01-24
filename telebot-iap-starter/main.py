from telegram import Update
from telegram.ext import Updater, MessageHandler, CommandHandler, CallbackContext, Filters
from itertools import zip_longest


# the colon helps with the type hinting. therefore the argument update: Update tells pyCharm what to hint.
# the -> None tells you that it doesn't return anything
# if you put -> str and u return a number, if can help u catch error
# you can also return a list of strings by first importing List from typing then put -> List[str]
def hello(update: Update, context: CallbackContext) -> None:
    print(update)
    firstName = update.message.from_user.first_name
    text = update.message.text
    sbEcho = spongeBobText(text)
    # 'from' is a python keyword and thus you user from_user instead
    update.message.reply_text(f'Whatupppp {firstName}')
    update.message.reply_text(f'{text}')
    update.message.reply_text(f'{sbEcho}')

def spongeBobText(txt):
    upper = txt[::2].upper()
    lower = txt[1::2].lower()
    changeText = "".join([u + l for u,l in zip_longest(upper,lower,fillvalue="")])
    return changeText

def add(update: Update, context: CallbackContext) -> None:
    # check for error statements and return. This is called guard statement.
    if len(context.args) != 2:
        update.message.reply_text(f"ERROR: You have to key in 2 arguments")
        return
    if not context.args[0].isnumeric() or not context.args[1].isnumeric():
        update.message.reply_text(f"ERROR: You have to key in 2 integers")
        return
    sum = int(context.args[0]) + int(context.args[1])
    update.message.reply_text(f'Sum is {sum}')



# Bot token here
updater = Updater('TOKEN')

# The updater has a dispatcher
# You add the handler; MessageHandler is the type of Handler; callback function is hello
# The filters.update handles EVERYTHING like messages, photos, stickers etc.
# filters.text will only filter texts
# callback function requires 2 arguments
updater.dispatcher.add_handler(CommandHandler("add", callback=add))
updater.dispatcher.add_handler(MessageHandler(Filters.update & Filters.chat_type.private & (~Filters.forwarded), callback=hello))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    updater.start_polling()
    updater.idle()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
