'''
Anybody can add commands, and edit them, can put pictures or texts but not both.
PS: if using pics , do not use short links, instead use those with extension. <Just a suggestion

Cog By Neophyte#5556

'''
import os
import re
import json
import myjson
import discord
import requests
from discord.ext import commands

class cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def is_owner(ctx):
        return (ctx.author.id == 280271578850263040 or ctx.author.id == 283413165381910539)

    def load_url(self):
        '''load the simple storage url'''
        with open("data/config.json") as f:
            link = json.load(f)
            if link["s_link"] == "link_here":
                storage_link = os.environ.get("s_link")
            else:
                storage_link = link["s_link"]
        return storage_link

    @commands.command()
    async def cmdadd(self, ctx,args:str = None, args1:str = None):
        '''add commands'''
        url = self.load_url()
        if args == None or args1 == None:
            await ctx.send("`Missing command.`")
            return
        else:
            data = myjson.get(url)
            data = json.loads(data)
            args = args.lower()
            if "{}".format(args) not in data:
                data["{}".format(args)] = {}
                data["{}".format(args)]["cmd"] = "{}".format(args1)
                data["{}".format(args)]["added_by"] = "{}".format(ctx.author)
                data["{}".format(args)]["author_id"] = "{}".format(ctx.author.id)
                url = myjson.store(json.dumps(data),update=url)
                em = discord.Embed(description = "Your command has been added :)")
                em.colour = discord.Colour.green()
                await ctx.send(embed = em)
            else:
                em = discord.Embed(description = "A similar command was added by **{}** which says **{}**. Do you really want to change it? type yes or no. Will only work if you are the one who added it :D".format(data["{}".format(args)]["added_by"], data["{}".format(args)]["cmd"]))
                em.colour = discord.Colour.green()
                await ctx.send(embed = em)
                def check(ctx):
                    return (ctx.content == 'yes' or ctx.content == 'no' or ctx.content == 'Yes' or ctx.content == 'No')
                msg = await self.bot.wait_for('message', check=check)
                msg.content = msg.content.lower()
                if msg.content == "yes" and data["{}".format(args)]["author_id"] == "{}".format(ctx.author.id):
                    data["{}".format(args)] = {}
                    data["{}".format(args)]["cmd"] = "{}".format(args1)
                    data["{}".format(args)]["added_by"] = "{}".format(ctx.author)
                    data["{}".format(args)]["author_id"] = "{}".format(ctx.author.id)
                    url = myjson.store(json.dumps(data),update=url)
                    em = discord.Embed(description = "The Command has been edited :)")
                    em.colour = discord.Colour.green()
                    await ctx.send(embed = em)
                else:
                    em = discord.Embed(description = "Edit command Terminated due to your selection or not being the one who added the command :D")
                    em.colour = discord.Colour.red()
                    await ctx.send(embed = em)

    @commands.command()
    async def cmd(self, ctx, *,args:str = None):
        '''get the command'''
        url = self.load_url()
        if args == None:
            await ctx.send("`Missing cmd name`")
        else:
            data = myjson.get(url)
            data = json.loads(data)
            args = args.lower()
            try:
                url = "{}".format(data["{}".format(args)]["cmd"])
                response = requests.head(url)
                resp_code = response.headers.get('content-type')
            #extentions = [".gif",".jpg",".webp",".png"]
            except Exception as e:
                #print(e)
                resp_code = 'xyzx xD'
            if "{}".format(args) in data:
                command = data["{}".format(args)]["cmd"]
                command_author = data["{}".format(args)]["added_by"]
                if "image" in resp_code:
                    em = discord.Embed()
                    em.set_image(url = command)
                    em.set_footer(text = "Added by {}".format(command_author))
                    await ctx.send(embed = em)
                else:
                    em = discord.Embed(description = command)
                    em.colour = discord.Colour.blue()
                    em.set_footer(text = "Added by {}".format(command_author))
                    await ctx.send(embed = em)
            else:
                em = discord.Embed(description = "No such commands found!")
                em.colour = discord.Colour.red()
                await ctx.send(embed = em)

    @commands.command()
    @commands.check(is_owner)
    async def storagelink(self, ctx):
        '''Get the link'''
        url = self.load_url()
        await ctx.send(url)

    @commands.command()
    async def allcmds(self, ctx):
        '''list of all commands added'''
        url = self.load_url()
        data = myjson.get(url)
        data = json.loads(data)
        key_for_count = list(data.keys())
        key = list(data.keys())
        key = '\n'.join(key[:20])
        current_count = len(key_for_count)
        command_list = "```py\nList will show only upto (20) commands, currently ({}):\n\n{}\n```".format(current_count,key)
        await ctx.send(command_list)

    @commands.command()
    @commands.check(is_owner)
    async def delcmd(self, ctx, *,args):
        '''Delete a command (owner only)'''
        try:
            url = self.load_url()
            data = myjson.get(url)
            data = json.loads(data)
            args = args.lower()
            if args in data:
                em = discord.Embed(description = "**{}** has been removed ,which was added by **{}**".format(args, data["{}".format(args)]["added_by"]))
                em.colour = discord.Colour.green()
                data.pop('{}'.format(args), None)
                url = myjson.store(json.dumps(data),update=url)
                await ctx.send(embed = em)
            else:
                em = discord.Embed(description = "No such command exists.")
                em.colour = discord.Colour.red()
                await ctx.send(embed =em)
        except Exception as e:
            #print(e)
            await ctx.send("`Error: 'key'`")


def setup(bot):
	bot.add_cog(cmds(bot))
