import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Define your bot token
TOKEN = "6752618609:AAFJufwcSl-i3CqOXjO4SXGi5NdHYP9BuVo"

# Define the function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! Send me a video file.')

# Define the function to handle video messages
def handle_video(update: Update, context: CallbackContext) -> None:
    video_file = update.message.video.get_file()
    file_id = video_file.file_id
    file_path = video_file.file_path
    file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"

    # Convert video file to HTTPS link
    response = requests.get(file_url)
    if response.status_code == 200:
        https_link = "https://stream.moviesmaster.org//converted_video.mp4"  # Replace with your HTTPS link
        update.message.reply_text(f"Here's the HTTPS link for your video: {https_link}")
    else:
        update.message.reply_text("Failed to convert the video.")

# Define the main function to run the bot
def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))

    # Register message handler for videos
    dispatcher.add_handler(MessageHandler(Filters.video, handle_video))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
