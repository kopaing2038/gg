import logging
from pyrogram import Client, filters
import boto3
from urllib.parse import quote

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

API_ID = '28679600'
API_HASH = '3d54e9caa473c838ed8762256afcb176'
BOT_TOKEN = "6752618609:AAFJufwcSl-i3CqOXjO4SXGi5NdHYP9BuVo"

# Create the Pyrogram client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# S3 Configuration
s3 = boto3.client('s3',
                  aws_access_key_id='31348d1b8b734ada5dc9fc302782d68c',
                  aws_secret_access_key='cdab26813ba4eefc74ce4da0b93e4243',
                  endpoint_url='https://sin1.contabostorage.com')

bucket_name = 'movieslist'  # Bucket name in your contabostorage server

# Define the function to handle the /start command
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text('Hi! Send me a video file.')

@app.on_message(filters.video)
async def handle_video(client, message):
    # Download the video file
    file_path = await message.download()
    
    # Upload the video file to the contabostorage server
    file_name = file_path.split('/')[-1]  # Extracting file name from the path
    s3.upload_file(file_path, bucket_name, file_name)
    
    # Generate HTTPS link
    https_link = f"https://sin1.contabostorage.com/{bucket_name}/{quote(file_name)}"
    
    # Respond with the converted HTTPS link
    await message.reply_text(f"Here's the HTTPS link for your video: {https_link}")

# Start the Bot
if __name__ == '__main__':
    app.run()
