import os
import discord
import requests
import json
from discord.ext import commands
import imgkit

#config = imgkit.config(wkhtmltoimage='/app/.apt/usr/local/bin/wkhtmltopdf/wkhtmltox_0.12.5-1.bionic_amd64.deb')

if 'DYNO' in os.environ:
    print ('loading wkhtmltopdf path on heroku')
    WKHTMLTOPDF_CMD = subprocess.Popen(
        ['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf-pack')], # Note we default to 'wkhtmltopdf' as the binary name
        stdout=subprocess.PIPE).communicate()[0].strip()
else:
    print ('loading wkhtmltopdf path on localhost')
    MYDIR = os.path.dirname(__file__)
    WKHTMLTOPDF_CMD = os.path.join(MYDIR + "/static/executables/bin/", "wkhtmltopdf.exe")

    

class newShot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @property
    def character_page_link(self):
        '''getting the character link'''
        with open("data/config.json") as f:
            link = json.load(f)
            if link["char_link"] == "link_here":
                char_link = os.environ.get("char_link")
            else:
                char_link = link["char_link"]
        return char_link

    @commands.command()
    async def sendshot(self,ctx, *, args:str = None):
        try:
            if args == None:
                await ctx.send(content = "`Missing name`")
                return
            link = self.character_page_link
            new_text = args.replace(' ','+')
            link = link+new_text
            imgkit.from_url(f'{link}', 'out.jpg')
            await ctx.send(file=discord.File('out.jpg'))
        except Exception as e:
            print(e)




def setup(bot):
    bot.add_cog(newShot(bot))
