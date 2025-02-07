import os
import asyncio
from pyrogram import Client, filters
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot configuration
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")

# Initialize MongoDB
mongo_client = AsyncIOMotorClient(MONGO_URI)
db = mongo_client["telegram_bot"]
users_collection = db["users"]

# Initialize bot
bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Start command
@bot.on_message(filters.command("start"))
async def start(client, message):
    user = {"user_id": message.from_user.id, "username": message.from_user.username}
    await users_collection.update_one({"user_id": user["user_id"]}, {"$set": user}, upsert=True)
    await message.reply_text("Hello! I'm a bot running 24x7 🚀")

# Run bot
bot.run()
