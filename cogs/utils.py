'''
by Noble#5556

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

class Utility(commands.Cog):
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
        general_commands = "\n`user`,`server`, `help` , `invite`, `about`, `avatar`, `banner`"
        #aq_commands = "`char`, `aq3ditem`, `aq3dserver`, `aq3dnews`, `aqwservers`"
        aq_commands = """i)AQ3D: `char`, `mchar`, `titles`, `aq3ditem`, `aq3dserver`, `aq3dnews(not stable always)`, `aq3dtitles`, `mtitles`, `title`\n\nii)AQW: `aqwbadges`, `aqwserver`, `aqwitem (buggy)`\n\niii)EpicDuel: `epchar` """
        #other_games = "\n`osu`"
        music_command = "\n`music`"
        moderation_commands = "**__NOTE__:** To use Moderation commands, the bot must have a role higher than the one to be used upon.\n\n`kick`, `ban`, `bans`, `mute`, `unban`, `unmute`, `addrole`, `removerole`"
        translator_commands = "\n`translator`"
        miscellaneous_commands = "\n`rng`,`emoji`,`rate`, `actions`, `cmdadd`, `cmd`, `allcmds`, `delcmd (owner only)`, `google`, `wikipedia`"
        welcome_commands = "\n`welcomemsg`, `togglewel`, `welview`,`leavemsg`, `toggleleave`, `settype`, `setbg`"
        anime_commands = "`\nanisearch`, `anidata`"
        further_help = "`\nexpand[command]`"
        #await ctx.send("**WILL BE DEVELOPED FURTHER:**\n"+"```\n"+help_cmd+"```")
        em = discord.Embed(title = "Commands List:", url = "https://winter-song-web.herokuapp.com/")
        em.set_thumbnail(url = self.bot.user.avatar_url)
        em.set_author(name = "Help Menu",url = "https://winter-song-web.herokuapp.com/" ,icon_url = "http://bestanimations.com/Nature/winter/winter-snow-nature-animated-gif-27.gif")
        em.add_field(name = "1.General:", value = general_commands,inline = False)
        em.add_field(name = "2.Moderation: ", value = moderation_commands ,inline = False)
        em.add_field(name = "3.AE: ", value = "**__NOTE__**: If you can't view the full char page in mobile using `w!char` use `w!mchar` and Mobile users use `w!mtitles` for titles list instead of `w!aq3dtitles`\n\n"+aq_commands ,inline = False)
        #em.add_field(name = "4.Other Games: ", value = other_games ,inline = False)
        #em.add_field(name = "5.Music ", value = music_command ,inline = False)
        em.add_field(name = "4.Translator:", value = translator_commands, inline = False)
        em.add_field(name = "5.Welcome/Leave", value = welcome_commands, inline = False)
        em.add_field(name = "6.Miscellaneous ", value =miscellaneous_commands ,inline = False)
        em.add_field(name = "7.Anime Stuff ", value =anime_commands ,inline = False)
        em.add_field(name = "8.Expanded help: ", value = further_help ,inline = False)
        em.add_field(name = "9.Report a problem: ", value = "If you have a suggestion or want something to be added or you want to report an error use:\n\n`report`",inline = False)
        em.add_field(name = "Talk to me: ", value = "You can talk to me! I learn as you talk. Currently I have less conversations but the more you talk the more I catch up (please be patient, I have a limit too ;-;), you can help me! To talk\n\n winter [something you want to say]",inline = False)
        em.add_field(name = "Support/Server:", value = "[Upvote The BOT!](https://discordbots.org/bot/385681784614027265)\n[Support Server](https://discord.gg/k3PKut6)", inline = False)
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
        elif args == 'banner':
            info = "Shows server banner."
            usage = "w!banner"
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
        elif args == 'osu':
            info = "Get Info about an osu! player."
            usage = "w!osu [username].\n**For Example:** w!osu Sylphynn\n\nPS: Thanks to Sylphynn#6329 for the quick help."
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
            usage = "w!char [someone]. Eg: w!char test\nNot all badges appear on mobile, so use w!mchar instead! :D"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'titles':
            info = "Gives aq3d character titles!"
            usage = "w!titles [someone]. Eg: w!titles test\nThis is not char page, use w!char for charpage."
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'mchar':
            info = "Gives aq3d character details. (Mobile Friendly)"
            usage = "w!mchar [someone]. Eg: w!mchar test\n\n*This doesn't show the character class picture."
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'aq3dtitles':
            info = "Gives a list of aq3d titles/achievements present at the moment in the game."
            usage = "w!aq3dtitles"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'mtitles':
            info = "Gives a list of aq3d titles/achievements present at the moment in the game. (Mobile Friendly)"
            usage = "w!mtitles"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'title':
            info = "Gives info about a title/achievement."
            usage = "w!title [titlename]. Eg: w!title Brutalcorn"
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
        elif args == 'aq3dptr':
            info = "Get AQ3D PTR details."
            usage = "w!aq3dptr.\n\nPTR: Public Testing Realm."
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
        elif args == 'rng':
            info = "Do a Random pick among choices!"
            usage = "w!rng 1,2,3,4"
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
            usage = """w!cmdadd [your command].\n\n**__For Example:__** w!cmdadd I am okay\n\nBesides texts, links can be used too, but not both together for the moment.\n\n **__PS:__** The Quotations are necessary and some image links might show up your image."""
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
            info = "Get the custom added command, if exists. (that you added)"
            usage = "w!cmd\n\nEg: w!cmd or w!cmd [id of someone who put a cmd]"
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
        elif args == 'anisearch':
            info = "Search Anime/Mangas To get expanded Data!"
            usage = "w!anisearch [query]\n\nEg: w!anisearch Naruto"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'anidata':
            info = "Get data about an anime/manga, searched before!"
            usage = "w!anidata [query]\n\nEg: w!anidata Naruto"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        elif args == 'welcomemsg':
            info = "Set a welcome message, Gets triggered when a new member joins in. Picture welcomes are in test, you can enable them using settype."
            usage = """The author has to have admin permissions (not the bot) i.e The Server owner or one with Administrative Permission.\n**Command:** w!welcomemsg "<your_message>" "<channel_id where to send it>"\n\n**__NOTE:__** You don't need to add server name in the message, it will be done automatically.\n\n**__Additional:__** without the channel id, it will post to the channel where the command was set.\n to toggle on/off of the welcome message, check **w!expand togglewel**.\n\n**__PS:__** The quotations in "<your_message>" "<channel_id where to send it>" are necessary and your custom message if you are using pic type must less than 50 characters."""
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            em.set_image(url = "https://image.ibb.co/jEVrX6/current.png")
            await ctx.send(embed = em,content = "**Currently:**\n")
        elif args == 'welview':
            info = "Have a preview of the welcome message that you set using me!"
            usage = "w!welview\n**Aliases:** welpreview\n\nw!preview [id] for owner (incase I forget XD)"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
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
        elif args == 'setbg':
            info = "Set the Background image for welcome picture"
            usage = "w!setbg [link]. **Default:** background picture set."
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
        elif args == 'report':
            info = "Report a problem or suggest something!"
            usage = "w!report [text].\nFor Example: w!report char page command isnt working!"
            em = discord.Embed()
            em.set_author(name = "Help Menu ['{}']".format(args), icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.add_field(name = "1.Info:", value = info,inline = False)
            em.add_field(name = "2.Usage: ", value = usage ,inline = False)
            em.colour = discord.Colour.green()
            em.set_footer(text = "|Winter-Song|",icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        else:
            em = discord.Embed()
            em.set_author(name = "Command doesn't exist.\nJoin Help Server, if you need help:\nhttps://discord.gg/k3PKut6", icon_url = "http://bestanimations.com/Science/Chemistry/chemistry-atom-proton-electron-animation-17.gif")
            em.colour = discord.Colour.red()
            await ctx.send(embed = em)


    @commands.command()
    async def rng(self, ctx, *, choices: commands.clean_content):
        '''choose! use , in between
        '''
        choices = choices.split(',')
        choices[0] = ' ' + choices[0]
        await ctx.send(str(random.choice(choices))[1:])

    @commands.command()
    async def banner(self, ctx, *, guild = None):
        """gets a guild's banner image
        """
        try:
            if guild is None:
                guild = ctx.guild
            elif type(guild) == int:
                guild = discord.utils.get(self.bot.guilds, id = guild)
            elif type(guild) == str:
                guild = discord.utils.get(self.bot.guilds, name = guild)
            banner = guild.banner_url_as(format = "png")
            async with ctx.session.get(str(banner)) as resp:
                image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file = discord.File(file, "banner.png"))
        except Exception as e:
            await ctx.send("`Banner wasn't found..`")

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
