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
import random
import pip
import os
import io


class Information:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, *, member : discord.Member=None):
        '''Returns someone's avatar url'''
        member = member or ctx.author
        av = member.avatar_url
        if ".gif" in av:
            av += "&f=.gif"
        color = await ctx.get_dominant_color(av)
        em = discord.Embed(url=av, color=color)
        em.set_author(name=str(member), icon_url=av)
        em.set_image(url=av)
        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            em_list = await embedtobox.etb(em)
            for page in em_list:
                await ctx.send(page)
            try:
                async with ctx.session.get(av) as resp:
                    image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, 'avatar.png'))
            except discord.HTTPException:
                await ctx.send(av)

    @commands.command(aliases=['servericon'], no_pm=True)
    async def serverlogo(self, ctx):
        '''Return the server's icon url.'''
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
        em.add_field(name='Playing:', value=user.game, inline = False)
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

        embed = discord.Embed()
        embed.colour = await ctx.get_dominant_color(ctx.author.avatar_url)

        embed.set_author(name='Winter-Song', icon_url=ctx.author.avatar_url)

        total_members = sum(1 for _ in self.bot.get_all_members())
        total_online = len({m.id for m in self.bot.get_all_members() if m.status is discord.Status.online})
        total_unique = len(self.bot.users)

        voice_channels = []
        text_channels = []
        for guild in self.bot.guilds:
            voice_channels.extend(guild.voice_channels)
            text_channels.extend(guild.text_channels)

        text = len(text_channels)
        voice = len(voice_channels)
        dm = len(self.bot.private_channels)

        now = datetime.datetime.utcnow()
        delta = now - self.bot.uptime
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        fmt = '{h}h {m}m {s}s'
        if days:
            fmt = '{d}d ' + fmt
        uptime = fmt.format(d=days, h=hours, m=minutes, s=seconds)
        embed.add_field(name='Author:', value='Quanta#5556 (N)', inline = False)
        embed.add_field(name='Uptime:', value=uptime, inline = False)
        embed.add_field(name='Guilds:', value=len(self.bot.guilds), inline = False)
        embed.add_field(name='Members:', value=f'{total_unique} total\n{total_online} online', inline = False)
        embed.add_field(name='Channels:', value=f'{text} text\n{voice} voice\n{dm} direct', inline = False)
        memory_usage = self.bot.process.memory_full_info().uss / 1024**2
        cpu_usage = self.bot.process.cpu_percent() / psutil.cpu_count()
        embed.add_field(name='Process: ', value=f'{memory_usage:.2f} MiB\n{cpu_usage:.2f}% CPU', inline = False)
        embed.set_footer(text='|Winter-Song|')
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self,ctx):
        '''invite the bot'''
        link = "https://discordapp.com/oauth2/authorize?client_id=385681784614027265&scope=bot&permissions=305196166"
        #em.set_author(name = "Thank You for using", icon_url = self.bot.user.avatar_url)
        await ctx.send("**Get me From:**\n"+link)

    @commands.command()
    async def music(self,ctx):
        '''Music commands'''
        help_cmd = """
            **__Music Commands:__**
        ```
1. m!summon: before using.
2. m!play [song]: play the song.
3. m!repeat: toggle repeat modes.
4. m!queue: songs in queue.
5. m!volume [value]: set volume.
6. m!promote [number]: put song to top.
7. m!disconnect [always do.]
        ```"""
        await ctx.send(help_cmd)
def setup(bot):
	bot.add_cog(Information(bot))
