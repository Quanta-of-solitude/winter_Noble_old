'''

Actual Cog from Selfbot, edited by Quanta#5556 (N)


'''


import discord
from discord.ext import commands
from urllib.parse import urlparse
from ext import embedtobox
import datetime
import asyncio
import psutil
from PIL import Image
import random
import os
import io


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["av"])
    async def avatar(self, ctx, *, member: discord.Member = None):

        format = "gif"
        member = member or ctx.author
        if member.is_avatar_animated() != True:
	        format = "png"
        avatar = member.avatar_url_as(format = format if format is not "gif" else None)
        async with ctx.session.get(str(avatar)) as resp:
            image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file = discord.File(file, f"DP.{format}"))
        #await ctx.delete()


    @commands.command(aliases=['servericon'], no_pm=True)
    async def serverlogo(self, ctx):
        '''Return the server's icon url.'''
        await ctx.trigger_typing()
        icon = ctx.guild.icon_url
        color = await ctx.get_dominant_color(icon)
        server = ctx.guild
        em = discord.Embed(color=color, url=icon)
        em.set_author(name=server.name, icon_url=icon)
        em.set_image(url=icon)
        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            em_list = await embedtobox.etb(em)
            for page in em_list:
                await ctx.send(page)
            try:
                async with ctx.session.get(icon) as resp:
                    image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, 'serverlogo.png'))
            except discord.HTTPException:
                await ctx.send(icon)

    @commands.command(aliases=['server','si','svi'], no_pm=True)
    @commands.guild_only()
    async def serverinfo(self, ctx, server_id : int=None):
        '''Server Info'''
        await ctx.trigger_typing()
        server = self.bot.get_server(id=server_id) or ctx.guild
        total_users = len(server.members)
        online = len([m for m in server.members if m.status != discord.Status.offline])
        text_channels = len([x for x in server.channels if isinstance(x, discord.TextChannel)])
        voice_channels = len([x for x in server.channels if isinstance(x, discord.VoiceChannel)])
        categories = len(server.channels) - text_channels - voice_channels
        passed = (ctx.message.created_at - server.created_at).days
        created_at = "{}. **({})** days ago.".format(server.created_at.strftime("%d %b %Y"), passed)
        colour = await ctx.get_dominant_color(server.icon_url)
        data = discord.Embed(colour=colour)
        data.add_field(name="Created: ", value= created_at, inline = False)
        data.add_field(name="Region", value=str(server.region), inline = False)
        data.add_field(name="Users", value="{}/{}".format(online, total_users), inline = False)
        data.add_field(name="Text Channels", value=text_channels, inline = False)
        data.add_field(name="Voice Channels", value=voice_channels, inline = False)
        data.add_field(name="Categories", value=categories, inline = False)
        data.add_field(name="Roles", value=len(server.roles), inline = False)
        data.add_field(name="Owner", value=str(server.owner), inline = False)
        data.set_footer(text="Server ID: " + str(server.id))
        data.set_author(name=server.name, icon_url=None or server.icon_url)
        data.set_thumbnail(url=None or server.icon_url)
        try:
            await ctx.send(embed=data)
        except discord.HTTPException:
            em_list = await embedtobox.etb(data)
            for page in em_list:
                await ctx.send(page)


    @commands.command(aliases=['ui'], no_pm=True)
    @commands.guild_only()
    async def user(self, ctx, *, member : discord.Member=None):
        '''Getting The user Information'''
        await ctx.trigger_typing()
        server = ctx.guild
        user = member or ctx.message.author
        avi = user.avatar_url
        roles = sorted(user.roles, key=lambda c: c.position)

        for role in roles:
            if str(role.color) != "#000000":
                color = role.color
        if 'color' not in locals():
            color = 0

        rolenames = ', '.join([r.name for r in roles if r.name != "@everyone"]) or 'None'
        time = ctx.message.created_at
        channel = ctx.channel
        user_name = user.name
        try:
            msg = await channel.history(limit = None).get(author__name='{}'.format(user_name))
            duration = time- msg.created_at
            seconds = duration.total_seconds()
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
            hours = int(hours)
            minutes = int(minutes)
            seconds = int(seconds)
            passer = (time- msg.created_at).days
            formatted_seen = "**{} hrs, {} mins and {} secs ago. |({}) days ago.|**".format(hours,minutes,seconds,passer)
        except Exception as e:
            #print(e)
            formatted_seen = "The user didn't type here, yet."
        passed = (ctx.message.created_at - user.created_at).days
        created_at = "{}.  **({})** days ago.".format(user.created_at.strftime("%d %b %Y"), passed)
        passed1 = (ctx.message.created_at - user.joined_at).days
        joined_at = "{}.  **({})** days ago.".format(user.joined_at.strftime("%d %b %Y"), passed1)
        member_number = sorted(server.members, key=lambda m: m.joined_at).index(user) + 1
        em = discord.Embed(colour=color, timestamp=time)
        em.add_field(name='Name:', value=user.name, inline = False)
        em.add_field(name='NickName:', value=user.nick, inline = False)
        em.add_field(name='Member No:',value=str(member_number), inline = False)
        em.add_field(name='Status:', value=user.status, inline = False)
        em.add_field(name='Playing:', value=user.activity, inline = False)
        em.add_field(name='Account Created:', value= created_at, inline = False)
        em.add_field(name='Join Date:', value=joined_at, inline = False)
        em.add_field(name='Last Seen on this channel:', value= formatted_seen, inline = False)
        em.add_field(name='Bot Account:', value=user.bot, inline = False)
        em.add_field(name='Roles:', value=rolenames, inline=False)
        em.set_footer(text='User ID: '+str(user.id))
        em.set_image(url=avi)
        em.set_author(name=user, icon_url=server.icon_url)

        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            em_list = await embedtobox.etb(em)
            for page in em_list:
                await ctx.send(page)

    @commands.command(aliases=['bot', 'info'])
    async def about(self, ctx):
        '''About The bot, info, usage, process'''
        await ctx.trigger_typing()
        embed = discord.Embed()
        embed.colour = await ctx.get_dominant_color(ctx.author.avatar_url)
        embed.set_author(name='Winter-Song', icon_url=ctx.author.avatar_url)
        total_members = sum(1 for _ in self.bot.get_all_members())
        total_online = len({m.id for m in self.bot.get_all_members() if m.status is discord.Status.online})
        total_unique = len(self.bot.users)
        description = "```I am a simple bot designed for general purposes!\nI was inactive for a while, I am fixing things on go. Sorry.Not a 100% complete bot, ongoing updates daily and adding features :D\nView my help command using w!help```"
        library_used = "```discord.py @rewrite```"
        embed.add_field(name='Owner:', value='```Made by: Noble#5556\nID: 280271578850263040\n```', inline = False)
        embed.add_field(name = 'Description:', value = description, inline = False)
        embed.add_field(name='Total Members:', value=f'{total_members}', inline = False)
        embed.add_field(name='Using:', value=library_used, inline = False)
        memory_usage = self.bot.process.memory_full_info().uss / 1024**2
        cpu_usage = self.bot.process.cpu_percent() / psutil.cpu_count()
        embed.add_field(name='Process: ', value=f'{memory_usage:.2f} MiB\n{cpu_usage:.2f}% CPU', inline = False)
        embed.set_thumbnail(url = "http://image.ibb.co/mHBRcG/amiwinter.jpg")
        embed.set_footer(text='|Winter-Song|' , icon_url = self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self,ctx):
        '''invite the bot'''
        await ctx.trigger_typing()
        em = "<https://discordapp.com/oauth2/authorize?client_id=385681784614027265&scope=bot&permissions=305196166>"
        em1 = "https://discord.gg/k3PKut6"
        upvote = "https://discordbots.org/bot/385681784614027265"
        await ctx.send("Get me from:\n"+em+"\n\nIf you are enjoying my bot so far, please upvote it:\n"+upvote+"\n\nIf you want to suggest something/or need help join:\n"+em1)


def setup(bot):
	bot.add_cog(Information(bot))
