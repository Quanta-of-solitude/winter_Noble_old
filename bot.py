'''
Winter-Song!

 by Neophyte#5556 (Noble)

'''
import os
import discord
import asyncio
from discord.ext import commands
from ext.context import CustomContext
import psutil
import re
import json
from collections import defaultdict
import datetime
import aiohttp

class NewBot(commands.Bot):
    '''
    A Bot Made by ~ Neophyte#5556
    '''
    mentions_transforms = {
          '@everyone': '@\u200beveryone',
          '@here': '@\u200bhere'
    }
    mention_pattern = re.compile('|'.join(mentions_transforms.keys()))

    def __init__(self, **attrs):
        super().__init__(command_prefix = self.get_pre)
        self.session = aiohttp.ClientSession(loop = self.loop)
        self._extentions = [x.replace('.py', '') for x in os.listdir('cogs') if x.endswith('.py')]
        self.remove_command('help')
        self.process = psutil.Process()
        self.commands_used = defaultdict(int)
        self.load_extensions()

    def load_extensions(self, cogs = None, path = 'cogs.'):
        '''Loading the Extentions ;)'''
        for extension in cogs or self._extentions:
            try:
                self.load_extension('{0}{1}'.format(path, extension))
                print('Loaded Extention: {}'.format(extension))
            except Exception as e:
                print('CannotLoad: {0}\n'
                      '{type(e).__name__}: {1}'.format(extension, e))

    @staticmethod
    async def get_pre(bot, message):
        '''GET THE PREFIX'''
        with open('data/config.json') as f:
            prefix = json.load(f).get('PREFIX')
        return os.environ.get('PREFIX') or prefix or 'r. '

    def restart(self):
        os.exev(sys.executable, ['python'] + sys.argv)


    @classmethod
    def init(bot, token = None):
        '''RUN THE BOT'''
        amibot = bot()
        with open('data/config.json') as f:
            config = json.load(f)
            if config["TOKEN"] == "your_token_here":
                token = os.environ.get("TOKEN")
                token = "{}".format(token)
            else:
                token = config["TOKEN"]
        try:
            amibot.run(token, bot = True, reconnect = True)
        except Exception as e:
            print(e)

    async def on_connect(self):
        print('-------------\n'+ 'Winter-Song Logged in!')

    async def on_ready(self):
        '''SET THE UPTIME'''
        self.uptime = datetime.datetime.utcnow()
        await self.change_presence(activity = discord.Game(name="w!help | ["+str(len(self.guilds))+"]"))

    async def on_command(self, ctx):
        cmd = ctx.command.qualified_name.replace(' ', '_')
        self.commands_used[cmd] +=1

    async def process_commands(self, message):
        '''Utilizing the CustomContext subclass'''
        ctx = await self.get_context(message, cls = CustomContext)
        if ctx.command is None:
            return
        await self.invoke(ctx)

    async def on_message(self, message):
        '''Ignore commands by self'''
        if message.author.id == self.user.id or message.author.bot == True:
            return
        if 'discord.gg' in message.content:
            if message.guild.id == 356157029074862081 and message.channel.id != 356518005313765379:    #For Night Watch server- On Request
                try:
                    await asyncio.sleep(2)
                    await message.delete()
                    await asyncio.sleep(2)
                    alert = await message.channel.send("{} Please, post your invite links only in <#356518005313765379>\n:smile:".format(message.author.mention))
                    await asyncio.sleep(20)
                    await alert.delete()
                except Exception as e:
                    pass
        await self.process_commands(message)

    def get_server(self, id):
        return discord.utils.get(self.guilds, id = id)


if __name__ == '__main__':
    NewBot.init()
