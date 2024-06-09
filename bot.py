import discord
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the bot token and webhook URL from environment variables
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
WELCOME_IMAGE_URL = os.getenv('WELCOME_IMAGE_URL')
FAREWELL_IMAGE_URL = os.getenv('FAREWELL_IMAGE_URL')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot connected as {client.user}')

@client.event
async def on_member_join(member):
    welcome_message = f"Welcome to the server, {member.mention}! We're glad to have you here."
    data = {
        "content": welcome_message,
        "embeds": [
            {
                "title": "Welcome!",
                "description": welcome_message,
                "image": {
                    "url": WELCOME_IMAGE_URL
                }
            }
        ]
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("Welcome message sent successfully.")
    else:
        print(f"Failed to send welcome message: {response.status_code}")

@client.event
async def on_member_remove(member):
    farewell_message = f"{member.name} has left the server. We hope to see you again!"
    data = {
        "content": farewell_message,
        "embeds": [
            {
                "title": "Goodbye!",
                "description": farewell_message,
                "image": {
                    "url": FAREWELL_IMAGE_URL
                }
            }
        ]
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("Farewell message sent successfully.")
    else:
        print(f"Failed to send farewell message: {response.status_code}")

client.run(BOT_TOKEN)
