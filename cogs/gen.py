''' A rewritten cog, consisting of old personal commands (just for fun) also has kiss, hug, slap commands.
PS: THIS ISNT CUSTOM COMMANDS

by Quanta#5556 (N)
'''
import os
import discord
import json
import random
from discord.ext import commands
from cleverwrap import CleverWrap


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
        await ctx.trigger_typing()
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
            await ctx.trigger_typing()
            em = discord.Embed(description = choices)
            em.colour = discord.Colour.dark_blue()
            #await ctx.trigger_typing()
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
4. $winter []: have a chat with the bot.\n
5. w!eball []: Ask 8ball something.\n
6. w!say []: Speak through the bot.\n
7. winter [text]: Talk with the bot!
        ```
        """
        await ctx.send(help_cmd)


def setup(bot):
	bot.add_cog(Gen(bot))
