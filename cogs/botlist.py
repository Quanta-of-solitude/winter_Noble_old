import os
import dbl
import discord
from discord.ext import commands
import json
import aiohttp
import asyncio
import logging


class DiscordBotsOrgAPI(commands.Cog):
    """Handles interactions with the discordbots.org API"""

    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.update_stats())


    async def update_stats(self):
        dbltoken = '{}'.format(os.environ.get("dbltokenT"))
        headers = {'Authorization' : dbltoken}
        while True:
            url = 'https://discordbots.org/api/bots/385681784614027265/stats'
            data = {'server_count': len(self.bot.guilds)}
            async with aiohttp.ClientSession() as session:
                async with session.post(url, data = data, headers = headers) as r:
                    if r.status == 200:
                        print("posted")
                    else:
                        print(r.status)
                await session.close()
            await asyncio.sleep(1800)


def setup(bot):
    global logger
    logger = logging.getLogger('bot')
    bot.add_cog(DiscordBotsOrgAPI(bot))
