from discord.ext import commands
import discord
import random

class Random:
    """Generate random uselessness."""
    def __init__(self,bot):
        self.bot = bot
        self.music = bot.get_cog('Music')

    @commands.command(pass_context=True, no_pm=True)
    async def coin(self, ctx):
        """50-50 coin flip"""


        result = "Heads!" if random.randint(0,1) > 0 else 'Tails!'
        await self.bot.send_message(ctx.message.channel, "<@{}>, {}".format(ctx.message.author.id,result))

    @commands.command(pass_context=True, no_pm=True)
    async def roll(self, ctx,  *, nr = 100):
        """random roll between 0 and a specified number.
        Default 100."""

        nr = max(0,nr)
        randnr = random.randint(0,nr)
        await self.bot.send_message(ctx.message.channel, "<@{}> rolled {}".format(ctx.message.author.id,randnr))

    @commands.command(pass_context=True, no_pm=True)
    async def pick(self, ctx,  *, options):
        """Beus picks one of the options you provide for him.
        Seperate each option with a |."""

        options = options.split('|')
        randnr = random.randint(0,len(options)-1)
        await self.bot.send_message(ctx.message.channel, "<@{}> picked **{}**".format(ctx.message.author.id,options[randnr]))
