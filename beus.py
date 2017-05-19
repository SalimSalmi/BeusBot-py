import asyncio
import os
import sys
sys.path.insert(0, "lib")
import logging
import logging.handlers
import traceback
import datetime
import subprocess
from lib.utils.Formatter import Formatter

try:
    assert sys.version_info >= (3, 5)
    from discord.ext import commands
    import discord
except ImportError:
    print("Beus requires Discord.py library.\n")
    sys.exit()
except AssertionError:
    print("Beus requires Python 3.5.\n")
    sys.exit()

import lib.conf.settings as settings

class Bot(commands.Bot):

    def __init__(self, *args, **kwargs):

        self.uptime = datetime.datetime.utcnow()
        self._message_modifiers = []
        self._intro_displayed = False
        self._shutdown_mode = None

        # logger_b = logging.getLogger('beus')
        # logger_b.setLevel(logging.WARNING)
        # handler = logging.FileHandler(filename='logs/beus.log', encoding='utf-8', mode='w')
        # handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s',datefmt="[%d/%m/%Y %H:%M]"))
        # logger_b.addHandler(handler)
        #
        # self.logger = logger_b
        #
        # logger_d = logging.getLogger('discord')
        # logger_d.setLevel(logging.WARNING)
        # handler = logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w')
        # handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s',datefmt="[%d/%m/%Y %H:%M]"))
        # logger_d.addHandler(handler)

        super().__init__(*args, command_prefix=settings.PREFIX, **kwargs)

    async def send_message(self, *args, **kwargs):
        if len(args) == 2:
            args = list(args)
            arg = args.pop()
            if isinstance(arg, discord.embeds.Embed):
                kwargs["embed"] = arg
            else:
                kwargs["content"] = arg
        return await super().send_message(*args, **kwargs)

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')


def main(bot):
    from lib.modules.General import General
    from lib.modules.Music import Music
    from lib.modules.Sounds import Sounds
    from lib.modules.Random import Random

    bot.add_cog(General(bot))
    bot.add_cog(Music(bot))
    bot.add_cog(Sounds(bot))
    bot.add_cog(Random(bot))

    bot.run(settings.TOKEN)

if __name__ == '__main__':
    bot = Bot(formatter=Formatter(show_check_failure=False), description="Beus bot :D")

    main(bot)
