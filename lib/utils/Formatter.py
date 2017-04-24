import itertools
import inspect
import textwrap
from discord.ext import commands
import discord

class Formatter(commands.HelpFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def format(self):
        max_width = self.max_name_size
        description = self.command.description if not self.is_cog() else inspect.getdoc(self.command)

        if isinstance(self.command, commands.Command):
            # Command
            cmd_name = self.get_command_signature()
            cmd_help = self.command.help if self.command.help else ''
            em = discord.Embed(title=cmd_name, description=cmd_help, colour=0xcccccc)
        elif self.is_bot():
            # All modules
            cmds_names = ''
            cmds_help = ''
            for name in self.command.cogs:
                cmd_wrapped = textwrap.fill(inspect.getdoc(self.command.cogs[name]).split('\n')[0],30)
                newlines = cmd_wrapped.count('\n') + 1
                cmds_names += name + ('\n' * newlines)
                cmds_help  += cmd_wrapped + '\n'
            em = discord.Embed(title='Modules', description='List all the things! Find out more by using the command help followed by a module or command name.', colour=0xcccccc)

            em.add_field(name='Module', value='**' + cmds_names + '**')
            em.add_field(name='Description', value=cmds_help)

        else:
            # Module
            cmds_names = ''
            cmds_help = ''
            for name, command in self.filter_command_list():
                if name in command.aliases:
                    # skip aliases
                    continue
                cmd_wrapped = textwrap.fill(command.short_doc,30)
                newlines = cmd_wrapped.count('\n') + 1
                cmds_names += name + ('\n' * newlines)
                cmds_help  += cmd_wrapped + '\n'
            em = discord.Embed(title=self.command.__class__.__name__, description=description, colour=0xcccccc)
            em.add_field(name='Command', value='**' + cmds_names + '**')
            em.add_field(name='Description', value=cmds_help)
        return [em]
