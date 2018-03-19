import os
import discord
from discord.ext import commands
import aiohttp
import asyncio
import logging

class BTList:
    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.update_stats())
    async def update_stats(self):
        dbltoken = '{}'.format(os.environ.get("dbltokenT"))
        headers = {'Authorization' : dbltoken}
        while True:
            logger.info('attempting to post server count')
            urlbot = 'https://discordbots.org/api/bots/' + str(self.bot.user.id) + '/stats'
            payload = {'server_count': len(self.bot.guilds)}
            async with aiohttp.ClientSession() as session:
                async with session.post(urlbot, data = payload, headers = headers) as r:
                    if r.status == 200:
                        print("K")
                        logger.info('posted server count ({})'.format(len(self.bot.guilds)))
                    else:
                        logger.exception('Failed to post server count\n{}: {}'.format(type(e).__name__, e))
                    await session.close()
                await asyncio.sleep(1800)


def setup(bot):
    global logger
    logger = logging.getLogger('bot')
    bot.add_cog(BTList(bot))
