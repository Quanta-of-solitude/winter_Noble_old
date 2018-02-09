'''
TO get the datas

cog by Quanta#5556
'''
import os
import discord
from discord.ext import commands
import json
import myjson

class Datas:
    '''Get all datas'''
    def __init__(self, bot):
        self.bot = bot

    async def have_permissions(ctx):
        return ctx.author.id == 280271578850263040 #<.<

    @commands.command()
    @commands.check(have_permissions)
    async def datawelcome(self,ctx):
        '''welcome datas'''
        url = "{}".format(os.environ.get("sw_link"))
        data = myjson.get(url)
        data = json.loads(data)
        data = json.dumps(data)
        try:
            out = await ctx.send("```js\n"+data+"```")
        except:
            paginated_text = ctx.paginate(data)
            for page in paginated_text:
                if page == paginated_text[-1]:
                    out = await ctx.send(f'```js\n{page}\n```')
                    break
                await ctx.send(f'```js\n{page}\n```')

    @commands.command()
    @commands.check(have_permissions)
    async def dataleave(self,ctx):
        '''leave datas'''
        url = "{}".format(os.environ.get("sle_link"))
        data = myjson.get(url)
        data = json.loads(data)
        data = json.dumps(data)

        try:
            out = await ctx.send("```js\n"+data+"```")
        except:
            paginated_text = ctx.paginate(data)
            for page in paginated_text:
                if page == paginated_text[-1]:
                    out = await ctx.send(f'```js\n{page}\n```')
                    break
                await ctx.send(f'```js\n{page}\n```')
    @commands.command()
    @commands.check(have_permissions)
    async def datatogglewel(self,ctx):
        '''welcome toggles datas'''
        url = "{}".format(os.environ.get("toggle_link"))
        data = myjson.get(url)
        data = json.loads(data)
        data = json.dumps(data)

        try:
            out = await ctx.send("```js\n"+data+"```")
        except:
            paginated_text = ctx.paginate(data)
            for page in paginated_text:
                if page == paginated_text[-1]:
                    out = await ctx.send(f'```js\n{page}\n```')
                    break
                await ctx.send(f'```js\n{page}\n```')

    @commands.command()
    @commands.check(have_permissions)
    async def datatoggleleave(self,ctx):
        '''toggle leaves datas'''
        url = "{}".format(os.environ.get("toggle2_link"))
        data = myjson.get(url)
        data = json.loads(data)
        data = json.dumps(data)

        try:
            out = await ctx.send("```js\n"+data+"```")
        except:
            paginated_text = ctx.paginate(data)
            for page in paginated_text:
                if page == paginated_text[-1]:
                    out = await ctx.send(f'```js\n{page}\n```')
                    break
                await ctx.send(f'```js\n{page}\n```')

    @commands.command()
    @commands.check(have_permissions)
    async def datamsgtype(self,ctx):
        '''typedatas'''
        url = "{}".format(os.environ.get("type_link"))
        data = myjson.get(url)
        data = json.loads(data)
        data = json.dumps(data)

        try:
            out = await ctx.send("```js\n"+data+"```")
        except:
            paginated_text = ctx.paginate(data)
            for page in paginated_text:
                if page == paginated_text[-1]:
                    out = await ctx.send(f'```js\n{page}\n```')
                    break
                await ctx.send(f'```js\n{page}\n```')

    @commands.command()
    @commands.check(have_permissions)
    async def databg(self,ctx):
        '''bg datas'''
        url = "{}".format(os.environ.get("bg_link"))
        data = myjson.get(url)
        data = json.loads(data)
        data = json.dumps(data)

        try:
            out = await ctx.send("```js\n"+data+"```")
        except:
            paginated_text = ctx.paginate(data)
            for page in paginated_text:
                if page == paginated_text[-1]:
                    out = await ctx.send(f'```js\n{page}\n```')
                    break
                await ctx.send(f'```js\n{page}\n```')
    @commands.command()
    @commands.check(have_permissions)
    async def datacmds(self,ctx):
        '''cmd datas'''
        url = "{}".format(os.environ.get("s_link"))
        data = myjson.get(url)
        data = json.loads(data)
        data = json.dumps(data)

        try:
            out = await ctx.send("```js\n"+data+"```")
        except:
            paginated_text = ctx.paginate(data)
            for page in paginated_text:
                if page == paginated_text[-1]:
                    out = await ctx.send(f'```js\n{page}\n```')
                    break
                await ctx.send(f'```js\n{page}\n```')

    @commands.command()
    @commands.check(have_permissions)
    async def dataautorole(self,ctx):
        '''auto role datas'''
        url = "{}".format(os.environ.get("ar_link"))
        data = myjson.get(url)
        data = json.loads(data)
        data = json.dumps(data)

        try:
            out = await ctx.send("```js\n"+data+"```")
        except:
            paginated_text = ctx.paginate(data)
            for page in paginated_text:
                if page == paginated_text[-1]:
                    out = await ctx.send(f'```js\n{page}\n```')
                    break
                await ctx.send(f'```js\n{page}\n```')

def setup(bot):
	bot.add_cog(Datas(bot))
