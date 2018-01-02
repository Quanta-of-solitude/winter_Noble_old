from Extras import MALsearch
from discord.ext import commands
import discord
from bs4 import BeautifulSoup as parse
import requests

class weeb:

    def __init__(self, bot):
        self.bot = bot
        self.search = MALsearch.MAL()

    def madeinfo(self, link):
        infos = []
        desc = []
        r= requests.get(link)
        s = parse(r.content, 'lxml')
        data1 = s.find("div", {"class": "fl-l score"}).attrs
        data1_rate = s.find("div", {"class": "fl-l score"}).get_text()
        data1_rate = data1_rate.replace(' ', '')
        data1_rate = data1_rate.replace('\n', '')
        data2_rank = s.find("span", {"class": "numbers ranked"}).get_text()
        data3_info = s.find("span",{"itemprop": "description"}).get_text()
        desc.append(data3_info)
        data4_episodes = s.find_all("div", {"class": "spaceit"})[0].get_text()
        data4_episodes = data4_episodes.replace('\n', '')
        data4_status = s.find_all("div", {"class": "spaceit"})[1].get_text()
        data4_status = data4_status.replace('\n', '')
        data4_air = s.find_all("div", {"class": "spaceit"})[2].get_text()
        data4_air = data4_air.replace('\n', '')
        data5_image = s.find("img", {"class": "ac"}, src = True)
        infos.append(data4_episodes+"\n"+data4_status+"\n"+data4_air)
        return {"users":data1["data-user"],"rating" : data1_rate, "rank": data2_rank, "inf": desc, "add": infos, "image": data5_image["src"]}

    @commands.command(aliases=['animesearch', 'searchanime'])
    async def anisearch(self, ctx, *,query:str = None):
        '''search top results'''
        try:
            if query == None:
                await ctx.send("`Error: Anime Name not provided!`")
                return
            await ctx.trigger_typing()
            result = self.search.asearch(query)
            info = "To get details about a result use w!anidata [result]"
            em = discord.Embed(title = "Anime Search Results:", url = "https://myanimelist.net/")
            em.add_field(name = "1.Top 7 Results:", value ="\n\n"+result, inline = False)
            em.add_field(name = "2.Expansion:", value ="\n\n"+info, inline = False)
            em.set_thumbnail(url = "https://t7.rbxcdn.com/fa9885c6d96569f6b7e33d908959089f")
            em.set_footer(text = "|Winter-Song|",icon_url = self.bot.user.avatar_url)
            em.colour = discord.Colour.blue()
            await ctx.send(embed = em)
        except Exception as e:
            print(e)
            await ctx.send("`Error: NONE!`")
    @commands.command(aliases=['animedata'])
    async def anidata(self, ctx, *,query:str = None):
        '''data about a result'''
        try:
            if query == None:
                await ctx.send("`Error: None has no result!`")
                return
            await ctx.trigger_typing()
            link = self.search.adata(query)
            print(link)
            datas = self.madeinfo(link)
            data_infos = '\n'.join(datas["add"])
            data_rate ="**"+datas["rating"]+"**"+" by "+datas["users"]
            data_syn = datas["inf"]
            data_syn = '\n'.join(data_syn)
            data_syn = data_syn[0:210]
            data_syn = data_syn+"....."
            #print(datas)
            em = discord.Embed(title = query, url = link)
            em.set_author(name = "Result", icon_url = ctx.author.avatar_url)
            em.colour = discord.Colour.red()
            em.set_thumbnail(url = "https://t7.rbxcdn.com/fa9885c6d96569f6b7e33d908959089f")
            em.set_footer(text = "|Winter-Song|",icon_url = self.bot.user.avatar_url)
            em.add_field(name = "Rating: ", value = data_rate, inline = True)
            em.add_field(name = "Rank: ", value = datas["rank"], inline = True)
            em.add_field(name = "About: ", value = data_infos, inline = False)
            em.add_field(name = "Sypnosis: ", value = data_syn, inline = False)
            try:
                em.set_image(url = datas["image"])
            except Exception as e:
                pass
            await ctx.send(embed = em)
        except Exception as e:
            print(e)
            await ctx.send("`Error: None Found!`")
def setup(bot):
    bot.add_cog(weeb(bot))
