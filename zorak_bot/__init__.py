__version__ = "0.1.0"
from discord.ext.commands import Bot

bot = Bot(command_prefix=["z.", "Z."])
bot.remove_command("help")
BOT = bot

