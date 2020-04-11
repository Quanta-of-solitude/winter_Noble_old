import os
import discord
import requests
import json
from discord.ext import commands
import imgkit

config = imgkit.config(wkhtmltoimage="./bin/wkhtmltopdf")



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

            with open("out.jpg", "rb") as file:
                url = "https://api.imgbb.com/1/upload"
                payload = {
                    "key": "{}".format(os.environ.get("imgkey")),
                    "image": base64.b64encode(file.read()),
                }

                res = requests.post(url, payload)
                got_file = res.content.decode()
                #print(got_file)
                got_file = json.loads(got_file)
                file = got_file["data"]["url_viewer"]
                file = file.replace("\/","//")
                em = discord.Embed()
                em.set_image(url = "{}".format(file))
                await ctx.send(embed =em)
                
        except Exception as e:
            print(e)




def setup(bot):
    bot.add_cog(newShot(bot))
