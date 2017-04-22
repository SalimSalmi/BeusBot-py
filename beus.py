import asyncio
import os
import sys
sys.path.insert(0, "lib")
import logging
import logging.handlers
import traceback
import datetime
import subprocess

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
