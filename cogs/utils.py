'''
Actual Cog from Selfbot, edited by Quanta#5556 (N)

PS: Help command shouldn't be here, but ¯\_(ツ)_/¯
'''
import discord
from discord.ext import commands
from discord.ext.commands import TextChannelConverter
from contextlib import redirect_stdout
from ext.utility import load_json
from urllib.parse import quote as uriquote
from lxml import etree
from ext import fuzzy
from ext import embedtobox
from PIL import Image
import unicodedata
import traceback
import textwrap
import aiohttp
import inspect
import asyncio
import time
import re
import io
import os
import random

class Utility:
    '''Useful commands to make your life easier'''
    def __init__(self, bot):
        self.bot = bot
        #self.lang_conv = load_json('data/langs.json')
        self._last_embed = None
        self._rtfm_cache = None
        self._last_google = None
        self._last_result = None

    async def is_owner(ctx):
        return ctx.author.id == 280271578850263040 #for the eval command, you can change to your own.


    @commands.command(name='logout')
    @commands.check(is_owner)
    async def _logout(self, ctx):
        '''
        Shuts down the bot,
        equi to a restart if you are hosting the bot on heroku.
        '''
        await ctx.send('`Logging out....`')
        await self.bot.logout()


    @commands.command(name='help')
    async def help(self, ctx):
        general_commands = "`user`, `server`, `help` , `invite`, `about`, `avatar`"
        #aq_commands = "`char`, `aq3ditem`, `aq3dserver`, `aq3dnews`, `aqwservers`"
        aq_commands = """i)AQ3D: `char`, `aq3ditem(buggy)`, `aq3dserver`, `aq3dnews`\nii)AQW: `aqwchar`, `aqwbadges`, `aqwserver`, `aqwitem (buggy)`\niii)EpicDuel: `epchar` """
        music_command = "`music`"
        moderation_commands = "**__NOTE__:** To use Moderation commands, the bot must have a role higher than the one to be used upon.\n\n`kick`, `ban`, `bans`, `mute`, `unban`, `unmute`, `addrole`, `removerole`"
        translator_commands = "`translator`"
        miscellaneous_commands = "`emoji`,`rate`, `actions`, `cmdadd`, `cmd`, `allcmds`, `delcmd (owner only)`, `google`, `wikipedia`"
        welcome_commands = "**__NOTE__**: Will be developed Futher, servers that enabled welcome messages before, are asked to set type using w!settype, for details check w!expand settype.\n\n`welcomemsg`, `togglewel`, `leavemsg`, `toggleleave`, `settype`"
        further_help = "`expand[command]`"
        #await ctx.send("**WILL BE DEVELOPED FURTHER:**\n"+"```\n"+help_cmd+"```")
        em = discord.Embed(title = "Commands List:", url = "https://winter-song-web.herokuapp.com/")
        em.set_thumbnail(url = self.bot.user.avatar_url)
        em.set_author(name = "Help Menu",url = "https://winter-song-web.herokuapp.com/" ,icon_url = "http://bestanimations.com/Nature/winter/winter-snow-nature-animated-gif-27.gif")
        em.add_field(name = "1.General:", value = general_commands,inline = False)
        em.add_field(name = "2.Moderation: ", value = moderation_commands ,inline = False)
        em.add_field(name = "3.AE: ", value = aq_commands ,inline = False)
        em.add_field(name = "4.Music ", value = music_command ,inline = False)
        em.add_field(name = "5.Translator:", value = translator_commands, inline = False)
        em.add_field(name = "6.Welcome/Leave", value = welcome_commands, inline = False)
        em.add_field(name = "7.Miscellaneous ", value =miscellaneous_commands ,inline = False)
        em.add_field(name = "8.Expanded help: ", value = further_help ,inline = False)
        em.colour = discord.Colour.blue()
        em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
        await ctx.send(content = "**Prefixes: w!, $**\n",embed = em)


    @commands.command()
    async def expand(self,ctx, *,args = None):
        '''expansion of help commands'''
        args = args.lower()
        if args == 'user':
            info = "Gives user details."
            usage = "w!user or ;user @mention. \n Example: w!user @someone"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'server':
            info = "Gives user details."
            usage = "w!server"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'help':
            info = "Shows the help menu."
            usage = "w!help"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'emoji':
            info = "Shows the help menu for emojis."
            usage = "w!emoji  or w!emojis"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'invite':
            info = "Get the bot."
            usage = "w!invite"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'about':
            info = "Shows the info about the bot."
            usage = "w!about"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'rate':
            info = "Get a werid rating graph about yourself. The Graph is always weird "
            usage = "w!rate.\n**For Example:** w!rate (for yourself) or w!rate @mention (for an user)."
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'avatar':
            info = "Get the avatar (pfp) of a user."
            usage = "w!avatar. Eg: w!avatar @someone"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'kick':
            info = "Kick someone from server"
            usage = "w!kick @someone.  Returns: Nothing, if you don't have permission."
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'ban':
            info = "Ban someone from the server."
            usage = "w!ban @someone, also exists unban.\nReturns: Nothing, if you don't have permission."
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'bans':
            info = "See bans (list) in the server."
            usage = "w!bans.  Returns: Nothing, if you don't have permission."
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'mute':
            info = "Mute someone in the server."
            usage = "w!mute @someone [time/s/m/h], also exists unmute.\nEg: w!mute @someone 10s.\nReturns: Nothing, if you don't have permission."
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'addrole':
            info = "add role to someone."
            usage = "w!addrole @someone role_name.  Returns: Nothing, if you don't have permission."
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'removerole':
            info = "Remove role from someone."
            usage = "w!removerole @someone role_name.  Returns: Nothing, if you don't have permission."
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'unban':
            info = "Unban someone from the server."
            usage = "w!unban id/name, also exists ban.\nReturns: Nothing, if you don't have permission."
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'unmute':
            info = "Unmute a muted."
            usage = "w!unmute @someone, also exists mute.\nReturns: Nothing, if you don't have permission."
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'char':
            info = "Gives aq3d character details."
            usage = "w!char [someone]. Eg: w!char test"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'aq3ditem':
            info = "Gives details about an aq3d item."
            usage = "w!aq3ditem [item]. Eg: w!aq3ditem vorah dagger"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'aqwitem':
            info = "Gives details about an aqw item"
            usage = "w!aqwitem [item]. Eg: w!aqwitem Amethyst Axe.\n\n**The names must be correctly used in order for this to work.**"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'aq3dserver':
            info = "Get AQ3D Server details."
            usage = "w!aq3dserver"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'aqwservers':
            info = "Get AQW Server details."
            usage = "w!aqwservers"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'aq3dnews':
            info = "Get AQ3D Recent News."
            usage = "w!aq3dnews.\nPS: will work only if api isn't down."
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'epchar':
            info = "Gives epicduel character details."
            usage = "w!epchar [someone]. Eg: w!epchar test"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'music':
            info = "Get music bot commands."
            usage = "w!music"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'translator':
            info = "Get available Translation commands!"
            usage = "w!translator"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'expand':
            info = "Get expanded help for commands."
            usage = "w!expand expand"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'actions':
            info = "Action commands, includes hug, slap, kiss. (mini-games coming soon)"
            usage = "w!actions. This will send the list of available commands based on actions and games"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'cmdadd':
            info = "Adding a custom command!"
            usage = """w!cmdadd "Key" "Value".\n\n**__For Example:__** w!cmdadd "Java" "A Programming Language."\n\nBesides texts, links can be used too, but not both together for the moment.\n\n **__PS:__** The Quotations are necessary and some image links might show up your image."""
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'allcmds':
            info = "Get the List of commands added! List Limit: 20"
            usage = "w!allcmds\nThis will show a list of commands added. Limit: 20 but commands above 20 can added."
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'delcmd':
            info = "Delete an Entry. Only Owner at the moment."
            usage = "w!delcmd [entry]"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'cmd':
            info = "Get the custom added command, if exists."
            usage = "w!cmd [text(key)]\n\nEg: w!cmd test"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'google':
            info = "Get google results!"
            usage = "w!google [query]\n\nEg: w!google google"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'aqwbadges':
            info = "Get badge list of a player!"
            usage = """w!aqwbadges "name".\n\n**There are two ways:**\n i)w!aqwbadges "name"\nii)w!aqwbadges "name" "amount".\n\nThere are many aqw badges and sometimes this makes it spammy, so with "amount" you can set the number of badges to display.\n\n**For Example:** w!aqwbadges "Eternal Hell" "10" and w!aqwbadges "Eternal Hell"\n\n**__Note:__** The quotations are necessary"""
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'aqwchar':
            info = "Get character details of an aqw player"
            usage = "w!aqwchar name_here.\n\n**Eg:** w!aqwchar testtypeho"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'wikipedia':
            info = "Get wikipedia results!"
            usage = "w!wiki [query]\n\nEg: w!wiki google"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'welcomemsg':
            info = "Set a welcome message, Gets triggered when a new member joins in. Picture welcomes are in test, you can enable them using settype."
            usage = """The author has to have admin permissions (not the bot) i.e The Server owner or one with Administrative Permission.\n**Command:** w!welcomemsg "<your_message>" "<channel_id where to send it>"\n\n**__NOTE:__** You don't need to add server name in the message, it will be done automatically.\n\n**__Additional:__** without the channel id, it will post to the channel where the command was set.\n to toggle on/off of the welcome message, check **w!expand togglemsg**.\n\n**__PS:__** The quotations in "<your_message>" "<channel_id where to send it>" are necessary and your custom message if you are using pic type must less than 50 characters."""
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            em.set_image(url = "https://image.ibb.co/jEVrX6/current.png")
            await ctx.send(embed = em,content = "**Currently:**\n")
        elif args == 'leavemsg':
            info = "Set a leave message, Gets triggered when a member is removed or leaves the guild. Picture leaves might be coming next, after this is implemented successfully."
            usage = """The author has to have admin permissions (not the bot) i.e The Server owner or one with Administrative Permission.\n**Command:** w!leavemsg "<your_message>" "<channel_id where to send it>"\n\n**__NOTE:__** You don't need to add server name in the message, it will be done automatically.\n\n**__Additional:__** without the channel id, it will post to the channel where the command was set.\n to toggle on/off of the welcome message, check **w!expand toggleleave**.\n\n**__PS:__** The quotations in "<your_message>" "<channel_id where to send it>" are necessary."""
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            em.set_image(url = "https://image.ibb.co/b7S2um/leave.png")
            await ctx.send(embed = em,content = "**Currently:**\n")
        elif args == 'togglewel':
            info = "Set the welcome message function to on/off"
            usage = "w!togglewel on  < To set it on.\nw!togglewel off <To set it off.\n\n**Default:** off"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'settype':
            info = "Set the welcome message function to text or pictorial!"
            usage = "w!settype text  < To set it to text types.\nw!settype pic <To set it to picture types.\n\n**Default:** text"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'toggleleave':
            info = "Set the leave message function to on/off"
            usage = "w!toggleleave on  < To set it on.\nw!toggleleave off <To set it off.\n\n**Default:** off"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        else:
            em = discord.Embed()
            em.set_author(name = "Command doesn't exist.", icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.colour = discord.Colour.red()
            await ctx.send(embed = em)

    @commands.command(pass_context=True, hidden=True, name='eval')
    @commands.check(is_owner)
    async def _eval(self, ctx, *, body: str):
        """eval the python code"""

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result,
            'source': inspect.getsource
        }

        env.update(globals())

        body = self.cleanup_code(body)
        #await self.edit_to_codeblock(ctx, body)
        stdout = io.StringIO()
        err = out = None

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
            return await err.add_reaction('\u2049')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()

            if ret is None:
                if value:
                    try:
                        out = await ctx.send(f'```py\n{value}\n```')
                    except:
                        paginated_text = ctx.paginate(value)
                        for page in paginated_text:
                            if page == paginated_text[-1]:
                                out = await ctx.send(f'```py\n{page}\n```')
                                break
                            await ctx.send(f'```py\n{page}\n```')
            else:
                self._last_result = ret
                try:
                    out = await ctx.send(f'```py\n{value}{ret}\n```')
                except:
                    paginated_text = ctx.paginate(f"{value}{ret}")
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'```py\n{page}\n```')
                            break
                        await ctx.send(f'```py\n{page}\n```')

        if out:
            await out.add_reaction('\u2705') #tick
        if err:
            await err.add_reaction('\u2049') #x


    #async def edit_to_codeblock(self, ctx, body):
        #msg = f'{ctx.prefix}eval\n```py\n{body}\n```'
        #await ctx.message.edit(content=msg)


    def cleanup_code(self, content):
        """removing the code block"""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    def get_syntax_error(self, e):
        if e.text is None:
            return f'```py\n{e.__class__.__name__}: {e}\n```'
        return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'

def setup(bot):
    bot.add_cog(Utility(bot))
