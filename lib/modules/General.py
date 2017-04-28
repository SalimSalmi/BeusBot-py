from discord.ext import commands
import discord
from time import sleep

class General:
    """General commands."""
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def countdown(self, count=3):
        """Counts down from a given number.
        Default 3, max 10, min 1."""
        count = min(max(count, 1),10)
        for i in range(count):
            await self.bot.say(count-i)
            sleep(1)
        await self.bot.say('Go!')
