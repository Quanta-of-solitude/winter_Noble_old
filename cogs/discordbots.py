import os
import dbl
import discord
from discord.ext import commands

import aiohttp
import asyncio
import logging


class DiscordBotsOrgAPI:
    """Handles interactions"""

    def __init__(self, bot):
        self.bot = bot
        self.token = '{}'.format(os.environ.get("dbl_t"))
        self.dblpy = dbl.Client(self.bot, self.token)
        self.bot.loop.create_task(self.update_stats())

    async def update_stats(self):
        """Updates count"""

        while True:
            logger.info('Post server count attempt')
            try:
                await self.dblpy.post_server_count()
                logger.info('Server count posted: ({})'.format(len(self.bot.guilds)))
            except Exception as e:
                logger.exception('Failed to post!\n{}: {}'.format(type(e).__name__, e))
            await asyncio.sleep(1850)


def setup(bot):
    global logger
    logger = logging.getLogger('bot')
    bot.add_cog(DiscordBotsOrgAPI(bot))
