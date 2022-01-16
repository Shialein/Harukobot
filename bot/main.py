import os
import discord
import logging
from discord.ext import commands


class TutorialBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Greetings
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Eingeloggt als {self.bot.user} ({self.bot.user.id})')

    # Reconnect
    @commands.Cog.listener()
    async def on_resumed(self):
        print('Bot wieder da')

    # Error Handlers
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # Uncomment line 26 for printing debug
        # await ctx.send(error)

        # Unknown command
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('WAs kannst du eigentlich? Das gibts nicht')

        # Bot does not have permission
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('Brauch mehr rechte sadge')


# Gateway intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True

# Bot prefix
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'),
                   description='Nur Eskalativer Bot', intents=intents)

# Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


TOKEN = os.getenv('DISCORD_TOKEN')

if __name__ == '__main__':
    # Load extension
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            bot.load_extension(f'commands.{filename[: -3]}')

    bot.add_cog(TutorialBot(bot))
    bot.run(token, reconnect=True)
