#for discord version 
import os
import discord
import json
import requests
from discord.ext import commands

class Apex(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def apex(self,ctx, platform:str=None,name:str = None, legend:str = None):

        if platform == None:
           await ctx.send("`You need to specify a platform: pc,psn,xbl`")
           return

        if name == None:
            await ctx.send("`You need to specify a player name`")
            return


        print(platform,name,legend)

        legendNames = []
        details = []
        plat = platform

        if platform.lower() == "pc":
            platform = "origin"



        try:
            link = "{}".format(os.environ.get("getmeapex"))
            link = link+"{pf}/{user}".format(pf=platform,user=name)

            headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
                       "TRN-Api-Key": "{}".format(os.environ.get("apexCode"))

                    }
            data = json.loads(requests.get(link,headers=headers).content)

        except Exception as e:
            print(e,"Before requesting")
            await ctx.send("`Error Encountered, sorry`")

        
        
        try:
            try:
                level = data["data"]["segments"][0]["stats"]["level"]["displayValue"]
                rank = data["data"]["segments"][0]["stats"]["rankScore"]["metadata"]["rankName"]
                rankIcon = data["data"]["segments"][0]["stats"]["rankScore"]["metadata"]["iconUrl"]
                score = data["data"]["segments"][0]["stats"]["rankScore"]["displayValue"]
                trackerLink = "https://apex.tracker.gg/profile/{pf}/{user}".format(pf=plat,user=name)
                if int(level) > 500:
                    level = 500
            except Exception as e:
                print(e,"parse section")
                await ctx.send("`You sure that player exists? I cannot find him/her in apex.tracker.gg`")
        
            playerEmbed = discord.Embed(title = "{}".format(name), url = trackerLink)
            playerEmbed.set_author(name = "Apex Legends",icon_url = "https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Apex_legends_cover.jpg/220px-Apex_legends_cover.jpg")
            playerEmbed.add_field(name = "**Level: **", value = level, inline = True)
            playerEmbed.add_field(name = "**Rank: **", value = rank, inline = True)
            playerEmbed.add_field(name = "**Rank Score: **", value = score, inline = True)
            
            seg = data["data"]["segments"]

            if legend == None:

                
                #print(seg[0]["type"])
                for i in range(0,len(seg)):
                    #print(seg[i])
                    overview =  seg[i]["type"]
                    if overview != "overview":
                        #print(seg[i]["metadata"]["name"])
                        legendNames.append(seg[i]["metadata"]["name"])
                        legendsInfo = '\n'.join(legendNames)

                playerEmbed.add_field(name = "**Information available for: **", value = legendsInfo, inline = False)
                playerEmbed.set_footer(text = "Apex Legends tracker",icon_url = self.bot.user.avatar_url)
                playerEmbed.set_thumbnail(url = rankIcon)
                playerEmbed.set_image(url = "https://cdn1.dotesports.com/wp-content/uploads/2019/03/11133753/cropped-apex-embed-about-legends.png")
                playerEmbed.color=discord.Colour.red()
                await ctx.send("You can check any of the following legend infos. Use w!apex [platform] [player] [legend name]",embed = playerEmbed)

            
            else:
                
                
                for i in range(0,len(seg)): 
                    overview =  seg[i]["type"]
                    if overview != "overview":
                        legendName = seg[i]["metadata"]["name"]
                        if legendName.lower() == legend.lower():     
                            img = seg[i]["metadata"]["bgImageUrl"]           
                            stats = seg[i]["stats"]
                            for i in stats:
                                itemName = stats[i]["displayName"]
                                details.append("{item}: {stat}".format(item = itemName,stat = stats[i]["displayValue"]))
                                formDetails = '\n'.join(details)

                playerEmbed.add_field(name = "**Details for {}: **".format(legend.capitalize()), value = formDetails, inline = False)
                playerEmbed.set_footer(text = "Apex Legends tracker",icon_url = self.bot.user.avatar_url)
                playerEmbed.set_thumbnail(url = rankIcon)
                playerEmbed.set_image(url = img)
                playerEmbed.color=discord.Colour.green()
                await ctx.send(embed = playerEmbed)

             
        
        except Exception as e:
            print(e,"In the body")
            await ctx.send("`If there's nothing abve then: Player's Banner is empty for the legend... or rate-limited maybe?(counter to be added)`")




def setup(bot):
	bot.add_cog(Apex(bot))
