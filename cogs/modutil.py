"""Mod COG"""

import discord
from discord.ext import commands
from urllib.parse import urlparse
import datetime
import asyncio
import random
import pip
import os
import io

class Mod:

    def __init__(self, bot):
        self.bot = bot


    async def format_mod_embed(self, ctx, user, success, method, duration = None, location=None):
        """defaults"""
        emb = discord.Embed(timestamp=ctx.message.created_at)
        emb.set_author(name=method.title(), icon_url=user.avatar_url)
        emb.color = await ctx.get_dominant_color(user.avatar_url)
        emb.set_footer(text=f'User ID: {user.id}')
        if success:
            if method == 'ban' or method == 'hackban':
                emb.description = f'{user} was just {method}ned.'
            elif method == 'unmute':
                emb.description = f'{user} was just {method}d.'
            elif method == 'mute':
                emb.description = f'{user} was just {method}d for {duration}.'
            else:
                emb.description = f'{user} was just {method}ed.'
        else:
            emb.description = f"I do not have the required permissions to {method} {user.name}."

        return emb

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason='Please write a reason!'):

        '''Kick someone from the server.'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.kick_members == True or ctx.message.author.id == 283413165381910539 or ctx.message.author.id == 280271578850263040:
            try:
                await ctx.guild.kick(member, reason=reason)
            except:
                success = False
            else:
                success = True

            emb = await self.format_mod_embed(ctx, member, success, 'kick')

            await ctx.send(embed=emb)

        else:
            okay = 'You do not have the required permissions to **KICK** members.'

            em = discord.Embed(timestamp=ctx.message.created_at)
            em.set_author(name= 'Unable To Kick', icon_url=ctx.author.avatar_url)
            em.add_field(name = '**:interrobang: No Permission :interrobang:**', value = okay, inline = False)
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.set_footer(text= '|Winter-Song|')

            await ctx.send(embed=em)


    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason='Please write a reason!'):
        '''Ban someone from the server.'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.ban_members == True or ctx.message.author.id ==280271578850263040 or ctx.message.author.id == 283413165381910539:
            try:
                await ctx.guild.ban(member, reason=reason)
            except:
                success = False
            else:
                success = True

            emb = await self.format_mod_embed(ctx, member, success, 'ban')

            await ctx.send(embed=emb)
        else:
            okay2 = 'You do not have the required permissions to **BAN** or **UNBAN** members.'

            em = discord.Embed(timestamp=ctx.message.created_at)
            em.set_author(name= 'Unable To Ban', icon_url=ctx.author.avatar_url)
            em.add_field(name = '**:interrobang: No Permission :interrobang:**', value = okay2, inline = False)
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.set_footer(text= '|Winter-Song|')

            await ctx.send(embed=em)
    @commands.command()
    async def clean(self, ctx, limit : int=15):
        '''Clean a number of bot messages (owners only defined..)'''
        if ctx.message.author.id == 280271578850263040 or ctx.message.author.id == 283413165381910539:
            await ctx.purge(limit=limit+1, check=lambda m: m.author == self.bot.user)

    @commands.command()
    async def unban(self, ctx, name_or_id, *, reason=None):
        '''Unban someone '''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.ban_members == True or ctx.message.author.id == 280271578850263040 or ctx.message.author.id == 283413165381910539:
            ban = await ctx.get_ban(name_or_id)
            try:
                await ctx.guild.unban(ban.user, reason=reason)
            except:
                success = False
            else:
                success = True

            emb = await self.format_mod_embed(ctx, ban.user, success, 'unban')

            await ctx.send(embed=emb)
        else:
            okay3 = 'You do not have the required permissions to **BAN** or **UNBAN** members.'

            em = discord.Embed(timestamp=ctx.message.created_at)
            em.set_author(name= 'Unable To Unban', icon_url=ctx.author.avatar_url)
            em.add_field(name = '**:interrobang: No Permission :interrobang:**', value = okay3, inline = False)
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.set_footer(text= '|Winter-Song|')

            await ctx.send(embed=em)

    @commands.command(aliases=['del','p','prune'])
    async def purge(self, ctx, limit : int, member:discord.Member=None):
        '''Clean a number of messages'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.manage_messages == True or ctx.message.author.id == 280271578850263040 or ctx.message.author.id == 283413165381910539:
            if member is None:
                await ctx.purge(limit=limit+1)
            else:
                async for message in ctx.channel.history(limit=limit+1):
                    if message.author is member:
                        await message.delete()
        else:
            okay4 = 'You do not have the required permissions to **Purge Messages**.'

            em = discord.Embed(timestamp=ctx.message.created_at)
            em.set_author(name= 'Unable To Purge', icon_url=ctx.author.avatar_url)
            em.add_field(name = '**:interrobang: No Permission :interrobang:**', value = okay4, inline = False)
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.set_footer(text= '|Winter-Song|')

            await ctx.send(embed=em)

    @commands.command()
    async def banlist(self, ctx):
        '''See a list of banned users in the guild'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.ban_members == True or ctx.message.author.id == 280271578850263040 or ctx.message.author.id == 283413165381910539:
            try:
                bans = await ctx.guild.bans()
            except:
                return await ctx.send('I dont have the perms to see bans.')

            em = discord.Embed(title=f'List of Banned Members ({len(bans)}):')
            em.description = ', '.join([str(b.user) for b in bans])
            em.color = await ctx.get_dominant_color(ctx.guild.icon_url)

            await ctx.send(embed=em)
        else:
            okay5 = 'You do not have the required permissions to **See Ban List**.'

            em = discord.Embed(timestamp=ctx.message.created_at)
            em.set_author(name= 'Error', icon_url=ctx.author.avatar_url)
            em.add_field(name = '**:interrobang: No Permission :interrobang:**', value = okay5, inline = False)
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.set_footer(text= '|Winter-Song|')

            await ctx.send(embed=em)



    @commands.command()
    async def baninfo(self, ctx, *, name_or_id):
        '''Check the reason of a ban from the audit logs.'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.ban_members == True or ctx.message.author.id == 280271578850263040 or ctx.message.author.id == 283413165381910539:
            ban = await ctx.get_ban(name_or_id)
            em = discord.Embed()
            em.color = await ctx.get_dominant_color(ban.user.avatar_url)
            em.set_author(name=str(ban.user), icon_url=ban.user.avatar_url)
            em.add_field(name='Reason', value=ban.reason or 'None')
            em.set_thumbnail(url=ban.user.avatar_url)
            em.set_footer(text=f'User ID: {ban.user.id}')

            await ctx.send(embed=em)
        else:
            okay6 = 'You do not have the required permissions to **See Ban infos**.'

            em = discord.Embed(timestamp=ctx.message.created_at)
            em.set_author(name= 'Error', icon_url=ctx.author.avatar_url)
            em.add_field(name = '**:interrobang: No Permission :interrobang:**', value = okay6, inline = False)
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.set_footer(text= '|Winter-Song|')

            await ctx.send(embed=em)


    @commands.command(aliases=['adrl','giverole'])
    async def addrole(self, ctx, member: discord.Member, *, rolename: str):
        '''Add a role to someone else.'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.manage_roles == True or ctx.message.author.id == 280271578850263040 or ctx.message.author.id == 283413165381910539:
            role = discord.utils.find(lambda m: rolename.lower() in m.name.lower(), ctx.message.guild.roles)
            if not role:
                return await ctx.send('That role does not exist.')
            try:
                await member.add_roles(role)
                await ctx.send(f'Added: `{role.name}`')
            except:
                await ctx.send("I don't have the perms to add that role.")
        else:
            await ctx.send('You Do Not Have The Required Permission To **Add Roles**.')



    @commands.command(aliases=['rmrl','rmrole'])
    async def removerole(self, ctx, member: discord.Member, *, rolename: str):
        '''Remove a role from someone else.'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.manage_roles == True or ctx.message.author.id == 280271578850263040 or ctx.message.author.id == 283413165381910539:
            role = discord.utils.find(lambda m: rolename.lower() in m.name.lower(), ctx.message.guild.roles)
            if not role:
                return await ctx.send('`That role does not exist.``')
            try:
                await member.remove_roles(role)
                await ctx.send(f'Removed: `{role.name}`')
            except:
                await ctx.send("I don't have the perms to remove that role.")
        else:
            await ctx.send('You Do Not Have The Required Permission To **Remove Roles**.')


    @commands.command()
    async def hackban(self, ctx, userid, *, reason=None):
        '''Ban someone not in the server'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.ban_members == True or ctx.message.author.id == 280271578850263040 or ctx.message.author.id == 283413165381910539:
            try:
                userid = int(userid)
            except:
                await ctx.send('Invalid ID!')

            try:
                await ctx.guild.ban(discord.Object(userid), reason=reason)
            except:
                success = False
            else:
                success = True

            if success:
                async for entry in ctx.guild.audit_logs(limit=1, user=ctx.guild.me, action=discord.AuditLogAction.ban):
                    emb = await self.format_mod_embed(ctx, entry.target, success, 'hackban')
            else:
                emb = await self.format_mod_embed(ctx, userid, success, 'hackban')
            await ctx.send(embed=emb)
        else:
            okay7 = 'You do not have the required permissions to **Ban** or **Unban** members.'

            em = discord.Embed(timestamp=ctx.message.created_at)
            em.set_author(name= 'Unable to Ban', icon_url=ctx.author.avatar_url)
            em.add_field(name = '**:interrobang: No Permission :interrobang:**', value = okay7, inline = False)
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.set_footer(text= '|Winter-Song|')

            await ctx.send(embed=em)


    @commands.command()
    async def mute(self, ctx, member:discord.Member, duration, *, reason=None):
        '''Denies someone from chatting in all text channels and talking in voice channels for a specified duration'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.manage_roles == True or ctx.message.author.id == 280271578850263040 or ctx.message.author.id == 283413165381910539:
            unit = duration[-1]
            if unit == 's':
                time = int(duration[:-1])
                longunit = 'seconds'
            elif unit == 'm':
                time = int(duration[:-1]) * 60
                longunit = 'minutes'
            elif unit == 'h':
                time = int(duration[:-1]) * 60 * 60
                longunit = 'hours'
            else:
                await ctx.send('Invalid Unit! Use `s`, `m`, or `h`.')
                return

            progress = await ctx.send('Muting user!')
            try:
                for channel in ctx.guild.text_channels:
                    await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(send_messages = False), reason=reason)

                for channel in ctx.guild.voice_channels:
                    await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(speak=False), reason=reason)
            except:
                success = False
            else:
                success = True

            emb = await self.format_mod_embed(ctx, member, success, 'mute', f'{str(duration[:-1])} {longunit}')
            progress.delete()
            await ctx.send(embed=emb)
            await asyncio.sleep(time)
            try:
                for channel in ctx.guild.channels:
                    await channel.set_permissions(member, overwrite=None, reason=reason)
            except:
                pass
        else:
            okay8 = 'You do not have the required permissions to **Mute** or **Unmute** members.'

            em = discord.Embed(timestamp=ctx.message.created_at)
            em.set_author(name= 'Unable to Mute', icon_url=ctx.author.avatar_url)
            em.add_field(name = '**:interrobang: No Permission :interrobang:**', value = okay8, inline = False)
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.set_footer(text= '|Winter-Song|')

            await ctx.send(embed=em)


    @commands.command()
    async def unmute(self, ctx, member:discord.Member, *, reason=None):
        '''Removes channel overrides for specified member'''
        if ctx.author.guild_permissions.administrator == True or ctx.author.guild_permissions.manage_roles == True or ctx.message.author.id == 280271578850263040 or ctx.message.author.id == 283413165381910539:
            progress = await ctx.send('Unmuting user!')
            try:
                for channel in ctx.message.guild.channels:
                    await channel.set_permissions(member, overwrite=None, reason=reason)
            except:
                success = False
            else:
                success = True

            emb = await self.format_mod_embed(ctx, member, success, 'unmute')
            progress.self.delete()
            await ctx.send(embed=emb)
        else:
            okay9 = 'You do not have the required permissions to **Mute** or **Unmute** members.'

            em = discord.Embed(timestamp=ctx.message.created_at)
            em.set_author(name= 'Unable to Mute', icon_url=ctx.author.avatar_url)
            em.add_field(name = '**:interrobang: No Permission :interrobang:**', value = okay9, inline = False)
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.set_footer(text= '|Winter-Song|')

            await ctx.send(embed=em)



def setup(bot):
	bot.add_cog(Mod(bot))
