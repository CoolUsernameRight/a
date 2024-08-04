import os
import discord
import asyncio
from dotenv import load_dotenv
from flask import Flask
import threading

app = Flask(__name__)

load_dotenv()

bot = discord.Bot()

@bot.slash_command(
    contexts={discord.InteractionContextType.private_channel},
    integration_types={discord.IntegrationType.user_install},
)
async def greet(ctx: discord.ApplicationContext, user: discord.User):
    await ctx.respond(f"Hello, {user}!")

@bot.slash_command(
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
)
async def say_hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hello!")

@bot.event
async def on_ready():
    print(f'Bot {str(bot.user)} works')

@app.route('/')
def index():
    return "Flask is working!"

def run_flask():
    app.run(host='0.0.0.0', port=5000)

async def start_bot():
    await bot.start(os.getenv("DISCORD_TOKEN"))

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    asyncio.run(start_bot())
