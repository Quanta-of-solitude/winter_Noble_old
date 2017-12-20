''' A rewritten cog, consisting of old personal commands (just for fun) also has kiss, hug, slap commands.
PS: THIS ISNT CUSTOM COMMANDS

by Quanta#5556 (N)
'''
import os
import discord
import asyncio
import json
import aiohttp
import async_timeout
import random
from random import randint
from discord.ext import commands
from cleverwrap import CleverWrap
import collections
bot = discord.Client()
c = collections.Counter()
class Gen:
    def __init__(self, bot):
        self.bot = bot
        self.client = discord.Client()



    @property
    def kiss_gif(self):
        links = ["http://i.imgur.com/0D0Mijk.gif", "http://i.imgur.com/TNhivqs.gif", "http://i.imgur.com/3wv088f.gif", "http://i.imgur.com/7mkRzr1.gif", "http://i.imgur.com/8fEyFHe.gif"]
        choice_made= random.choice(links)
        return choice_made
    @property
    def slap_gif(self):
        links = ["http://imgur.com/Lv5m6cb.gif", "http://i.imgur.com/BsbFQtz.gif", "http://i.imgur.com/hyygFya.gif", "http://i.imgur.com/XoHjIlP.gif"]
        choice_made= random.choice(links)
        return choice_made
    @property
    def hug_gif(self):
        links = ["http://i.imgur.com/sW3RvRN.gif", "http://i.imgur.com/gdE2w1x.gif", "http://i.imgur.com/zpbtWVE.gif", "http://i.imgur.com/ZQivdm1.gif", "http://i.imgur.com/MWZUMNX.gif"]
        choice_made= random.choice(links)
        return choice_made

    @property
    def cleverbot_Key(self):

        with open("data/config.json") as f:
            cl_key = json.load(f)
            if cl_key["cleverbot_key"] == "api_key_here":
                key_cl = os.environ.get("cleverbot_key")
            else:
                key_cl = cl_key["cleverbot_key"]

        return key_cl



    @commands.command()
    async def kiss(self, ctx, *, args:str = None):
        '''Kissing gif send,'''
        if args == None:
            await ctx.send("**Love is in the air, but... you cannot kiss the air**")
        else:
            kiss = self.kiss_gif
            em = discord.Embed()
            em.set_image(url = "{}".format(kiss))
            await ctx.send(content = "**{0} got kissed by {1.mention}**".format(args, ctx.message.author), embed =em)


    @commands.command()
    async def slap(self, ctx, *, args:str = None):
        '''slapping gif send,'''
        if args == None:
            await ctx.send("`Usage: w!slap [someone]`")
        else:
            kiss = self.slap_gif
            em = discord.Embed()
            em.set_image(url = "{}".format(kiss))
            await ctx.send(content = "**{0} got slapped by {1.mention}**".format(args, ctx.message.author), embed =em)

    @commands.command()
    async def hug(self, ctx, *, args:str = None):
        '''hugging gif send,'''
        if args == None:
            await ctx.send("`Usage: w!hug [someone]`")
        else:
            kiss = self.hug_gif
            em = discord.Embed()
            em.set_image(url = "{}".format(kiss))
            await ctx.send(content = "**{0} got hugged by {1.mention}**".format(args, ctx.message.author), embed =em)


    @commands.command()
    async def ter(self, ctx, *, args:str = None):
        if args == None:
            return
        cl_key = self.cleverbot_Key
        cl_load = CleverWrap("{}".format(cl_key))
        cl_resp = cl_load.say("{}".format(args))
        await ctx.send(content = cl_resp)
        cl_load.reset()

    @commands.command(aliases=['8ball','eightball'])
    async def eball(self, ctx, *, args:str = None):
        if args == None:
            await ctx.send("`Usage: w!eball [question]`")
        else:
            choices=["As I see it, yes", "It is certain", "It is decidedly so", "Most likely", "Outlook good",
                     "Signs point to yes", "Without a doubt", "Yes", "Yes – definitely", "You may rely on it", "Reply hazy, try again",
                     "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                     "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
            choices = random.choice(choices)
            em = discord.Embed(description = choices)
            em.colour = discord.Colour.dark_blue()
            await ctx.send(embed = em)

    @commands.command(aliases=['speak','talk'])
    async def say(self, ctx, *, args:str = None):
        '''repeats what you say'''
        await ctx.send(args)



    @commands.command(aliases=['action'])
    async def actions(self,ctx):
        '''help regarding action commands'''
        help_cmd = """
        **__Action Commands:__**
        ```
1. w!kiss []: Kiss an user, or anything. :T \n
2. w!slap []: Slap an user, or anything.  \n
3. w!hug []: Hug an user, or anything.  \n
4. w!gif []: Search a gif!\n
5. $winter []: have a chat with the bot.\n
6. w!eball []: Ask 8ball something.\n
7. w!say []: Speak through the bot.\n
8. winter [text]: Talk with the bot!
        ```
        """
        await ctx.send(help_cmd)

    @commands.command()
    async def gif(self, ctx, *, args:str = None):
        try:
            if args == None:
                await ctx.send("`Error: You didn't provide any search terms ._.`")
                return
            new_text = args.replace(' ','+')
            link = "http://api.giphy.com/v1/gifs/search?&api_key={}&q={}".format("jitNZKDvBDjzBMpTyH7D3aRhb5kpXUhA", new_text)
            random_entry = randint(1, 20)
            em = discord.Embed()
            async def fetch(session, url):
                with async_timeout.timeout(10):
                    async with session.get(url) as response:
                        return await response.json()
            async with aiohttp.ClientSession() as session:
                result = await fetch(session, link)
                #result = await r.json()
                if result["data"]:
                    em.set_image(url = "{}".format(result["data"][random_entry]['images']['fixed_height']['url']))
                    await ctx.send(embed =em)
                else:
                    await ctx.send("`Error: No results Found .-.`")
        except Exception as e:
            await ctx.send("`Some Internal error, sorry :sweat_smile:`")


    '''
    @commands.command()
    async def test(self,ctx,*, member: discord.Member = None):
        user = member
        user_name = user.name
        dates = []

        for channels in ctx.guild.text_channels:
            msg = await channels.history(limit = None).get(author__name='{}'.format(user_name))
            if msg != None:
                dates.append(msg.created_at)

        new = [d.strftime('%m-%d-%Y (%H hours and %M mins ago)') for d in dates]
        print(new)'''


def setup(bot):
	bot.add_cog(Gen(bot))
