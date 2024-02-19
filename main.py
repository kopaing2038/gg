import logging
from pyrogram import Client, filters
import urllib.parse

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
async def start(client, message):
    await message.reply_text('Hi! Send me a video file.')

@app.on_message(filters.video)
async def handle_video(client, message):
    # Download the video file
    file_path = await message.download()
    
    # Replace this with your conversion logic
    https_link = f"https://sin1.contabostorage.com/c9f9c005075244e3a2f88a4b113161c1:movieslist/{urllib.parse.quote(file_path)}"

    
    # Respond with the converted HTTPS link
    await message.reply_text(f"Here's the HTTPS link for your video: {https_link}")

# Start the Bot
if __name__ == '__main__':
    app.run()
