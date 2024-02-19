import logging
from pyrogram import Client, filters
import urllib.parse
import boto3

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

API_ID = '28679600'
API_HASH = '3d54e9caa473c838ed8762256afcb176'
BOT_TOKEN = "6752618609:AAFJufwcSl-i3CqOXjO4SXGi5NdHYP9BuVo"

# Create the Pyrogram client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# S3 configuration
s3_config = {
    'endpoint_url': 'https://sin1.contabostorage.com',
    'region_name': 'sin1',  # Change if necessary
}

s3_access_key_id = '31348d1b8b734ada5dc9fc302782d68c'  # Replace with your access key ID
s3_secret_access_key = 'cdab26813ba4eefc74ce4da0b93e4243'  # Replace with your secret access key

s3 = boto3.client('s3', 
                  aws_access_key_id=s3_access_key_id,
                  aws_secret_access_key=s3_secret_access_key,
                  **s3_config)

bucket_name = 'movieslist'  # Change to your bucket name


# Define the function to handle the /start command
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text('Hi! Send me a video file.')


@app.on_message(filters.video)
async def handle_video(client, message):
    # Download the video file
    file_path = await message.download()
    
    # Upload the video file to S3-compatible storage
    file_name = file_path.split("/")[-1]  # Extracting file name from path
    s3.upload_file(file_path, bucket_name, file_name)
    
    # Generate HTTPS link for the uploaded file
    https_link = f"https://{bucket_name}.{s3_config['endpoint_url']}/{urllib.parse.quote(file_name)}"
    
    # Respond with the converted HTTPS link
    await message.reply_text(f"Here's the HTTPS link for your video: {https_link}")


# Start the Bot
if __name__ == '__main__':
    app.run()
