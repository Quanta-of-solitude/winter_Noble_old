import requests
import asyncio
import os
import discord
from discord.ext import commands

class DBList:
    def __init__(self,bot):
        self.bot = bot
        self.bot.loop.create_task(self.update_stats())

    async def update_stats(self):
        dbltoken = "{}".format(os.environ.get("dbltokenT"))
        headers = {"Authorization": dbltoken}
        while True:
            id_self = str(self.bot.user.id)
            urlbot = "https://discordbots.org/api/bots/%s/stats"%(id_self)
            data = {'server_count': len(self.bot.guilds)}
            r = requests.post(urlbot, params = data, headers = headers)
            if r.status_code == 200:
                print("Posted count!")
            else:
                print("ERROR!")
            await asyncio.sleep(1800)

def setup(bot):
    bot.add_cog(DBList(bot))
