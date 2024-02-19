
import requests
import logging
from pyrogram import Client, filters
import requests


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


API_ID = '28679600'
API_HASH = '3d54e9caa473c838ed8762256afcb176'
BOT_TOKEN = "6752618609:AAFJufwcSl-i3CqOXjO4SXGi5NdHYP9BuVo"

# Create the Pyrogram client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Define the function to handle the /start command
@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text('Hi! Send me a video file.')

@app.on_message(filters.video)
def handle_video(client, message):
    file_id = message.video.file_id
    file_path = client.get_download_location(file_id)
    file_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"

    # Convert video file to HTTPS link
    response = requests.get(file_url)
    if response.status_code == 200:
        https_link = "https://stream.moviesmaster.org/converted_video.mp4"  # Replace with your HTTPS link
        message.reply_text(f"Here's the HTTPS link for your video: {https_link}")
    else:
        message.reply_text("Failed to convert the video.")

# Start the Bot
if __name__ == '__main__':
    app.run()


