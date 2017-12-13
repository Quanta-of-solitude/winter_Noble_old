'''
Cog by Quanta#5556
'''
import discord
from discord.ext import commands
import os
import myjson
import json
import asyncio


class Welcomer:

    def __init__(self, bot):
        self.bot = bot

    async def have_permissions(ctx):
        return (ctx.author.guild_permissions.administrator == True or ctx.author.id == 280271578850263040)

    def load_url(self):
        '''load the welcome storage url'''
        with open("data/config.json") as f:
            link = json.load(f)
            if link["sw_link"] == "link_here":
                storage_link = os.environ.get("sw_link")
            else:
                storage_link = link["sw_link"]
        return storage_link

    def toggle_url(self):
        '''load the welcome storage url'''
        with open("data/config.json") as f:
            link = json.load(f)
            if link["toggle_link"] == "link_here":
                storage_link = os.environ.get("toggle_link")
            else:
                storage_link = link["toggle_link"]
        return storage_link


    @commands.command()
    @commands.check(have_permissions)
    async def welcomemsg(self,ctx, args:str = None, args1:str = None):
        '''set the welcome msg  Syntax w!welcomemsg msg channelid'''
        server = ctx.guild
        url = self.load_url()
        url1 = self.toggle_url()
        if args == None:
            msg = "Welcome to {}".format(server)
        else:
            msg = args
        if args1 == None:
            channel_id = ctx.channel.id
        else:
            channel_id = args1
        data = myjson.get(url)
        data = json.loads(data)
        data1 = myjson.get(url1)
        data1 = json.loads(data1)
        if "{}".format(server.id) not in data:
            data["{}".format(server.id)] = {}
            data["{}".format(server.id)]["msg"] = "{}".format(msg)
            data["{}".format(server.id)]["channel_id"] = "{}".format(channel_id)
            data1["{}".format(server.id)] = {}
            data1["{}".format(server.id)]["set_welcome"] = "no"
            url = myjson.store(json.dumps(data),update=url)
            url1 = myjson.store(json.dumps(data1),update=url1)
            em = discord.Embed(description = "Welcome message has been set")
            em.colour = discord.Colour.green()
            await ctx.send(embed = em)
        else:
            em = discord.Embed(description = "There is a welcome msg (already set), do you want to change it? Reply yes or no")
            em.colour = discord.Colour.green()
            await ctx.send(embed = em)
            def check(ctx):
                return (ctx.content == 'yes' or ctx.content == 'no' or ctx.content == 'Yes' or ctx.content == 'No')
            msge = await self.bot.wait_for('message', check=check)
            msge.content = msge.content.lower()
            if msge.content == "yes":
                data["{}".format(server.id)] = {}
                data["{}".format(server.id)]["msg"] = "{}".format(msg)
                data["{}".format(server.id)]["channel_id"] = "{}".format(channel_id)
                data1["{}".format(server.id)] = {}
                data1["{}".format(server.id)]["set_welcome"] = "off"
                url = myjson.store(json.dumps(data),update=url)
                url1 = myjson.store(json.dumps(data1),update=url1)
                em = discord.Embed(description = "Welcome message has been set")
                em.colour = discord.Colour.green()
                await ctx.send(embed = em)
            else:
                em = discord.Embed(description = "Edit command Terminated :D")
                em.colour = discord.Colour.red()
                await ctx.send(embed = em)

    @commands.command()
    @commands.check(have_permissions)
    async def togglemsg(self,ctx, *,args:str = None):
        '''Toggle welcome or not'''
        url = self.toggle_url()
        data = myjson.get(url)
        data = json.loads(data)
        accepted = ["on", "of"]
        if args == None:
            data["{}".format(ctx.guild.id)] = {}
            data["{}".format(ctx.guild.id)]["set_welcome"] = "on"
            url = myjson.store(json.dumps(data),update=url)
            await ctx.send("`Welcome Message Enabled For The Server`")
        else:
            args = args.lower()
            if args in accepted:
                data["{}".format(ctx.guild.id)] = {}
                data["{}".format(ctx.guild.id)]["set_welcome"] = "{}".format(args)
                url = myjson.store(json.dumps(data),update=url)
                await ctx.send("`Welcome message set to: {}`".format(args))
            else:
                await ctx.send("`Error: Invalid Parameter, define on or off.`")

    async def on_member_join(self,member):
        '''welcome!'''
        try:
            server = member.guild
            user = member
            url_toggle = self.toggle_url()
            url_message = self.load_url()
            data_toggle = myjson.get(url_toggle)
            data_toggle = json.loads(data_toggle)
            data_message = myjson.get(url_message)
            data_message = json.loads(data_message)
            channel_id = data_message["{}".format(server.id)]["channel_id"]
            msg = data_message["{}".format(server.id)]["msg"]
            channel = self.bot.get_channel(int(channel_id))
            member_number = sorted(server.members, key=lambda m: m.joined_at).index(user) + 1
            if data_toggle["{}".format(server.id)]["set_welcome"] == "on":
                await channel.send("{}".format(msg)+"\n\n**Member:** {0.mention}".format(member)+"\n**Server:** **{}**".format(server.name)+"\n**Member No:** {}".format(member_number))
        except Exception as e:
            print(e)

def setup(bot):
	bot.add_cog(Welcomer(bot))
