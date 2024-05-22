
import datetime
import html
import logging

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram.constants import ParseMode

from my_modules.abc_modules import bot_config

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)





async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    time_send = update.message.date
    time_send = time_send + datetime.timedelta(hours= 5, minutes= 30)
    formatted_time = time_send.strftime('%Y-%m-%d %H:%M:%S')
    text = formatted_time + f"\n You send me any file i will send you the size of the file in appropriate size🍌🍌🍌"
    await context.bot.send_message(user.id, f"{formatted_time}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)



def format_file_size(size_in_bytes):
    if size_in_bytes < 1024:
        return f"{size_in_bytes} bytes"
    elif size_in_bytes < 1024 ** 2:
        size_in_kb = size_in_bytes / 1024
        return f"{size_in_kb:.2f} KB"
    elif size_in_bytes < 1024 ** 3:
        size_in_mb = size_in_bytes / (1024 ** 2)
        return f"{size_in_mb:.2f} MB"
    else:
        size_in_gb = size_in_bytes / (1024 ** 3)
        return f"{size_in_gb:.2f} GB"

# file_size_in_bytes = 10310
# formatted_size = format_file_size(file_size_in_bytes)
# print(f"File Size: {formatted_size}")


async def doc_fun(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user
    document = update.message.document
    doc_size_str = format_file_size(document.file_size)
    text = (f"Hello {html.escape(user.full_name)} You have send me a file with the size of "
            f"<blockquote>{doc_size_str}</blockquote> "
            f"Its full bytes size is: <code>{document.file_size}</code> "
            f"Please resend a new document for size checking"
            )
    await context.bot.send_message(user.id, text, parse_mode= ParseMode.HTML)


from telegram.constants import ChatAction
import asyncio
async def get_file_123(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    if len(context.args) != 1:
        await context.bot.send_message(user.id, f"Please send me in correct format")
        return
    file_id = context.args[0]
    try:
        text = f"Hello <b>{html.escape(user.full_name)}</b> This is Your document\n\n"
        await context.bot.send_document(user.id, file_id, caption=text, parse_mode=ParseMode.HTML)
    except Exception as e:
        print("Send Document from the file id is not possible")
    try:
        photo_id = "AgACAgUAAxkBAAJ6PGZN7iXR_g-WtcNoLz467HKH6XvrAAIOvDEbexlwVqUuMIR6jvUiAQADAgADeQADNQQ"
        text = f"Hello <b>{html.escape(user.full_name)}</b> This image you get as document is not found\n\n"
        await context.bot.send_photo(user.id, photo_id, caption=text, parse_mode=ParseMode.HTML)
    except Exception as e:
        await context.bot.send_message(user.id, f"An error occurred: {e}\nAdditionally, the fallback attempt failed: {e}")
    try:
        await context.bot.send_message(bot_config.ADMIN_IDS[0], f"There are some problem in the message when the {user.full_name} send the message:'{update.message.text}' ")
    except:
        print(f"at {datetime.datetime.now()} {user.full_name} has send a {update.message.text}")






async def get_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    if len(context.args) != 1:
        await context.bot.send_message(user.id, "Please send me in the correct format")
        return
    
    file_id = context.args[0]
    photo_id = "AgACAgUAAxkBAAJ6PGZN7iXR_g-WtcNoLz467HKH6XvrAAIOvDEbexlwVqUuMIR6jvUiAQADAgADeQADNQQ"
    text_document = f"Hello <b>{html.escape(user.full_name)}</b> This is your document\n\n"
    text_photo = f"Hello <b>{html.escape(user.full_name)}</b> This image is provided because the document was not found\n\n"
    error_admin_msg = f"There was a problem when {user.full_name} sent the message: '{update.message.text}'"
    
    try:
        await context.bot.send_document(user.id, file_id, caption=text_document, parse_mode=ParseMode.HTML)
    except Exception as e1:
        print(f"Send Document from the file id is not possible due to {e1}")
        try:
            await context.bot.send_photo(user.id, photo_id, caption=text_photo, parse_mode=ParseMode.HTML)
        except Exception as e2:
            print(f"Send photo is not possible due to {e2}")
            try:
                await context.bot.send_message(bot_config.ADMIN_IDS[0],error_admin_msg)
            except Exception as e3:
                print(f"An error occurred at {datetime.datetime.now()} when {user.full_name} sent a message: '{update.message.text}'. Additional error: {e3}")



async def get_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    if len(context.args) != 1:
        await context.bot.send_message(user.id, "Please send me in the correct format")
        return
    file_id = context.args[0]
    
    try:
        text_document = f"Hello <b>{html.escape(user.full_name)}</b> This is your document\n\n"
        await context.bot.send_document(user.id, file_id, caption=text_document, parse_mode=ParseMode.HTML)
    except Exception as e1:
        print(f"Sending document with file_id failed: {e1}")
        try:
            photo_id = "AgACAgUAAxkBAAJ6PGZN7iXR_g-WtcNoLz467HKH6XvrAAIOvDEbexlwVqUuMIR6jvUiAQADAgADeQADNQQ"
            text_photo = f"Hello <b>{html.escape(user.full_name)}</b> This image is provided because the document was not found\n\n"
            await context.bot.send_photo(user.id, photo_id, caption=text_photo, parse_mode=ParseMode.HTML)
        except Exception as e2:
            print(f"Sending photo failed: {e2}")
            try:
                error_admin_msg = f"There was a problem when {user.full_name} sent the message: '{update.message.text}'"
                await context.bot.send_message(bot_config.ADMIN_IDS[0], error_admin_msg)
            except Exception as e3:
                print(f"An error occurred at {datetime.datetime.now()} when {user.full_name} sent a message: '{update.message.text}'. Additional error: {e3}")







def main() -> None:
    """Start the bot."""
    application = Application.builder().token("🍌🍌🍌`").build()

    application.add_handler(CommandHandler("start", start_cmd))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler(
        command= ["get_file"],
        callback= get_file,
        filters= filters.ChatType.PRIVATE,
        block= False,
    ))

    application.add_handler(MessageHandler(filters.Document.ALL, doc_fun))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
