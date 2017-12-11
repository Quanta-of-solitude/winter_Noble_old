import discord
from discord.ext import commands
from mtranslate import translate

"""translate Cog. ~Quanta #5556"""

class Translate:

    def __init__(self,bot):
        self.bot = bot

    def translate_to_english(self, text):
        to_translate = text
        return translate(to_translate)
    def translate_to_espanol(self, text):
        to_translate = text
        return translate(to_translate,'es')
    def translate_to_korean(self, text):
        to_translate = text
        return translate(to_translate,'ko')
    def translate_to_chinese(self, text):
        to_translate = text
        return translate(to_translate,'zh')
    def translate_to_japanese(self, text):
        to_translate = text
        return translate(to_translate,'ja')
    def translate_to_german(self, text):
        to_translate = text
        return translate(to_translate,'de')
    def translate_to_croatian(self, text):
        to_translate = text
        return translate(to_translate,'hr')
    def translate_to_tagalog(self, text):
        to_translate = text
        return translate(to_translate,'fil')
    def translate_to_malay(self, text):
        to_translate = text
        return translate(to_translate,'ms')
    def translate_to_greek(self, text):
        to_translate = text
        return translate(to_translate,'el')

    def translate_to_hindi(self, text):
        to_translate = text
        return translate(to_translate,'hi')

    @commands.command()
    async def en(self, ctx, *,args:str = None):
        '''Translate to english'''
        if args == None:
            await ctx.send("`Error: nothing to translate`")
        else:
            translated_text = self.translate_to_english(args)
            await ctx.send("**Translated:** "+translated_text)

    @commands.command()
    async def es(self, ctx, *,args:str = None):
        '''Translate to espanol'''
        if args == None:
            await ctx.send("`Error: nothing to translate`")
        else:
            translated_text = self.translate_to_espanol(args)
            await ctx.send("**Translated:** "+translated_text)

    @commands.command()
    async def ko(self, ctx, *,args:str = None):
        '''Translate to korean'''
        if args == None:
            await ctx.send("`Error: nothing to translate`")
        else:
            translated_text = self.translate_to_korean(args)
            await ctx.send("**Translated:** "+translated_text)

    @commands.command()
    async def zh(self, ctx, *,args:str = None):
        '''Translate to chinese'''
        if args == None:
            await ctx.send("`Error: nothing to translate`")
        else:
            translated_text = self.translate_to_chinese(args)
            await ctx.send("**Translated:** "+translated_text)

    @commands.command()
    async def ja(self, ctx, *,args:str = None):
        '''Translate to japanese'''
        if args == None:
            await ctx.send("`Error: nothing to translate`")
        else:
            translated_text = self.translate_to_japanese(args)
            await ctx.send("**Translated:** "+translated_text)

    @commands.command()
    async def hr(self, ctx, *,args:str = None):
        '''Translate to croatian'''
        if args == None:
            await ctx.send("`Error: nothing to translate`")
        else:
            translated_text = self.translate_to_croatian(args)
            await ctx.send("**Translated:** "+translated_text)

    @commands.command()
    async def de(self, ctx, *,args:str = None):
        '''Translate to deutch'''
        if args == None:
            await ctx.send("`Error: nothing to translate`")
        else:
            translated_text = self.translate_to_german(args)
            await ctx.send("**Translated:** "+translated_text)

    @commands.command()
    async def ms(self, ctx, *,args:str = None):
        '''Translate to malay'''
        if args == None:
            await ctx.send("`Error: nothing to translate`")
        else:
            translated_text = self.translate_to_malay(args)
            await ctx.send("**Translated:** "+translated_text)

    @commands.command()
    async def el(self, ctx, *,args:str = None):
        '''Translate to greek'''
        if args == None:
            await ctx.send("`Error: nothing to translate`")
        else:
            translated_text = self.translate_to_greek(args)
            await ctx.send("**Translated:** "+translated_text)

    @commands.command()
    async def fil(self, ctx, *,args:str = None):
        '''Translate to tagalog'''
        if args == None:
            await ctx.send("`Error: nothing to translate`")
        else:
            translated_text = self.translate_to_tagalog(args)
            await ctx.send("**Translated:** "+translated_text)

    @commands.command()
    async def hi(self, ctx, *,args:str = None):
        '''Translate to hindi'''
        if args == None:
            await ctx.send("`Error: nothing to translate`")
        else:
            translated_text = self.translate_to_hindi(args)
            await ctx.send("**Translated:** "+translated_text)

    @commands.command()
    async def translator(self, ctx):
        '''help commands'''
        commands = """```
        Syntax = w!+code

Languages       |        code
----------------|---------------------------------
1.English       | en <text> convert to English.
                |
2.Spanish       | es <text> convert to Spanish.
                |
3.Japanese      | ja <text> convert to Japanese.
                |
4.Greek         | el <text> convert to Greek.
                |
5.Chinese       | zh <text> convert to Chinese.
                |
6.German        | de <text> convert to German.
                |
7.Fillipino     | fil <text> convert to Tagalog.
                |
8.Malay         | ms <text> convert to Malay.
                |
9.Croatian      | hr <text> convert to Croatian.
                |
10.Korean       | ko <text> convert to Korean.
                |
11.Hindi        | hi <text> convert to hindi.
```"""
        await ctx.send("**Translation Tools:**\n"+commands)




def setup(bot):
	bot.add_cog(Translate(bot))
