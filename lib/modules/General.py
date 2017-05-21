from discord.ext import commands
import discord
from time import sleep
import datetime

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

    @commands.command()
    async def uptime(self):
        """Show Beus' uptime."""
        since = self.bot.uptime.strftime("%Y-%m-%d %H:%M:%S")
        passed = self.get_bot_uptime()
        message = discord.Embed(description="**{}**".format(passed),color=0x30b030)
        await self.bot.say(embed=message)

    def get_bot_uptime(self, *, brief=False):
        # Courtesy of Danny
        now = datetime.datetime.utcnow()
        delta = now - self.bot.uptime
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        if not brief:
            if days:
                fmt = '{d} days, {h} hours, {m} minutes, and {s} seconds'
            else:
                fmt = '{h} hours, {m} minutes, and {s} seconds'
        else:
            fmt = '{h}h {m}m {s}s'
            if days:
                fmt = '{d}d ' + fmt

        return fmt.format(d=days, h=hours, m=minutes, s=seconds)
