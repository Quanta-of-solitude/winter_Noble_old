''''
emoji related  ~ Quanta#5556
'''

import os
import discord
import random
from discord.ext import commands
import io

class Emojis:

    def __init__(self, bot):
        self.bot = bot

    def check_emojis(self, bot_emojis, emoji):
        for exist_emoji in bot_emojis:
            if emoji[0] == "<" or emoji[0] == "":
                if exist_emoji.name.lower() == emoji[1]:
                    return [True, exist_emoji]
            else:
                if exist_emoji.name.lower() == emoji[0]:
                    return [True, exist_emoji]
        return [False, None]

    @commands.command(invoke_without_command=True, aliases=['emotelink', 'linkemoji'])
    async def emojilink(self, ctx, *, emoji: str = None):
        '''Get link to the emoji! -for mobile users'''
        try:
            if emoji == None:
                await ctx.send("`Error: No emoji detected`")
                return
            emoji = emoji.split(":")
            emoji_check = self.check_emojis(ctx.bot.emojis, emoji)
            if emoji_check[0]:
                emo = emoji_check[1]
            await ctx.send(emo.url)
        except Exception as e:
            await ctx.send("`Error: That isn't an emoji!`")

    @commands.command(aliases=['attach', 'link'])
    async def linkify(self,ctx):
        ''''link to your attachment -mobile users'''
        try:
            link = ctx.message.attachments[0].url
            await ctx.send(link)
        except Exception as e:
            await ctx.send("`No attachments detected!`")

    @commands.command(invoke_without_command=True, aliases=['emoteget', 'findemoji'])
    async def getemoji(self, ctx, *, emoji: str = None):
        '''Use emojis from other server in the bot'''
        try:
            if emoji == None:
                await ctx.send("`Error: Emoji name not Provided..`")
                return
            emoji = emoji.split(":")
            emoji_check = self.check_emojis(ctx.bot.emojis, emoji)
            if emoji_check[0]:
                emo = emoji_check[1]
            else:
                emoji = [e.lower() for e in emoji]
                if emoji[0] == "<" or emoji[0] == "":
                    emo = discord.utils.find(lambda e: emoji[1] in e.name.lower(), ctx.bot.emojis)
                else:
                    emo = discord.utils.find(lambda e: emoji[0] in e.name.lower(), ctx.bot.emojis)
                if emo == None:
                    em = discord.Embed(title="NULL", description="`Didn't find one`")
                    em.color = await ctx.get_dominant_color(ctx.author.avatar_url)
                    await ctx.send(embed=em)
                    return
            async with ctx.session.get(emo.url) as resp:
                image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, 'emoji_found.png'))
        except Exception as e:
            pass

    @commands.command(aliases=['helpemoji', 'emojihelp', 'emojis'])
    async def emoji(self,ctx):
        '''commands'''
        commands = """
**__Emoji Help Commands(will be developed further):__**\n
```
1. emojilink : Get the link of an emoji!(good for mobile users)
    Aliases: emotelink, linkemoji

2. getemoji: Get an emoji! the emoji must be in a server with the bot.
    Aliases: findemoji, emoteget

3. linkify: Get link of an attachment. (good for mobile users)
    Aliases: attach, link

4. emoji: Get the help menu.
    Aliases: helpemoji, emojihelp, emojis
```
"""
        await ctx.send(commands)
def setup(bot):
	bot.add_cog(Emojis(bot))
