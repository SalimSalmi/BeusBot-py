from discord.ext import commands
import discord

class Sounds:
    """Audio memes."""
    def __init__(self,bot):
        self.bot = bot
        self.music = bot.get_cog('Music')
        self.playing = False

    @commands.command(pass_context=True, no_pm=True)
    async def goat(self, ctx):
        """A goat screams."""
        await self.bot.say(":pepegoat:")
        await self.short_sound('./data/audio/sounds/goat.mp3', ctx)

    @commands.command(pass_context=True, no_pm=True)
    async def meep(self, ctx):
        """You get a meep."""
        await self.bot.say("meep")
        await self.short_sound('./data/audio/sounds/meep.mp3', ctx)

    @commands.command(pass_context=True, no_pm=True)
    async def noot(self, ctx):
        """Noot noot."""
        await self.bot.say("noot")
        await self.short_sound('./data/audio/sounds/noot.mp3', ctx)

    @commands.command(pass_context=True, no_pm=True)
    async def rawr(self, ctx):
        """Beus' magnificent cry."""
        await self.bot.say("rawr!")
        await self.short_sound('./data/audio/sounds/rawr.mp3', ctx)

    async def short_sound(self, song : str, ctx):

        if self.playing is True:
            return

        self.playing = True

        state = self.music.get_voice_state(ctx.message.server)

        if state.voice is None:
            success = await ctx.invoke(self.music.join)
            if not success:
                return

        def interupt():
            self.playing = False
            if state.is_playing():
                state.player.resume()
            else:
                state.toggle_next()

        try:
            await ctx.invoke(self.music.pause)
            player = state.voice.create_ffmpeg_player(song, after=interupt)
            player.start()
        except Exception as e:
            fmt = 'An error occurred while processing this request: ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
