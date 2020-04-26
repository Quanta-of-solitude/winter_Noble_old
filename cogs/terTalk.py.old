import discord
import os
import urllib.parse
import random
import requests
import json
from discord.ext import commands



class talktTest(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def ter(self, ctx,*,text:str=None):
        try:

            sessionids = "{}".format(os.environ.get("winterID"))

            chatLink = "{}".format(os.environ.get("winterLink"))+f"{sessionids}&q=Test"
            f = requests.post(chatLink)
            data = f.content.decode()
            data = json.loads(data)
            code = data["code"]

            if code == 0:
                
                await ctx.trigger_typing()
                query = urllib.parse.quote(text)
                chatLink = "{}".format(os.environ.get("winterLink"))+f"{sessionids}&q={query}"
                fetch = requests.get(chatLink)
                fetch = fetch.content.decode()
                fetch = json.loads(fetch)
                response = fetch["response"]
                await ctx.send(response)

            else:
                print(code)

        except Exception as e:
            print(e)



def setup(bot):
    bot.add_cog(talktTest(bot))
