from interactions import Client, Intents, listen
from interactions.ext import prefixed_commands
import traceback
from dotenv import load_dotenv
import os
import logging
import Funtions.config as cfg

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig()
cls_log = logging.getLogger("MyLogger")
cls_log.setLevel(logging.DEBUG)

bot = Client(
    token=TOKEN,
    intents=Intents.DEFAULT | Intents.MESSAGE_CONTENT | Intents.GUILD_MESSAGES | Intents.GUILDS |
    Intents.GUILD_INVITES | Intents.GUILD_MEMBERS | Intents.ALL,
    sync_interactions=True,
    asyncio_debug=True,
    logger=cls_log,
)
prefixed_commands.setup(bot, default_prefix="!")


@listen()
async def on_ready():
    print("Ready")
    print(f"This bot is owned by {bot.owner}")


bot.load_extension("Commands.ping")
bot.load_extension("Commands.verify")
bot.load_extension("Commands.join_lad")
bot.load_extension("Commands.join_servo")
bot.load_extension("Events.welcome")

try:
    bot.start()
except Exception as e:
    traceback.print_exc()
