import os
import dbl
import discord
from discord.ext import commands
import json
import aiohttp
import asyncio
import logging


class DiscordBotsOrgAPI:
    """Handles interactions with the discordbots.org API"""

    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.update_stats())


    async def update_stats(self):
        dbltoken = '{}'.format(os.environ.get("dbltokenT"))
        headers = {'Authorization' : dbltoken}
        while True:
            urlbot = 'https://discordbots.org/api/bots/385681784614027265/stats'
            payload = {'server_count': len(self.bot.guilds)}
            async with aiohttp.ClientSession() as session:
                async with session.post(urlbot, data = json.dumps(payload), headers = headers) as r:
                    if r.status == 200:
                        print("POSTED")
                await session.close()
            await asyncio.sleep(3600)


def setup(bot):
    global logger
    logger = logging.getLogger('bot')
    bot.add_cog(DiscordBotsOrgAPI(bot))
