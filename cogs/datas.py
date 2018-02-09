'''
TO get the datas

cog by Quanta#5556
'''
import os
import discord
from discord.ext import commands
import json
import uuid
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

    @commands.command()
    async def report(self,ctx, *,rep:str = None):
        if rep == None:
            await ctx.send("`Nothing provided!`")
            return
        else:
            url_rep = "{}".format(os.environ.get("reported_reports"))
            url_list = "{}".format(os.environ.get("reported_renames"))
            name = myjson.get(url_list)
            name = json.loads(name)
            data = myjson.get(url_rep)
            data = json.loads(data)
            UnId = str(uuid.uuid4())[:8]
            data[f"{UnId}"] = {}
            data[f"{UnId}"]["report"] = rep
            data[f"{UnId}"]["by"] = "{}".format(ctx.author)
            data[f"{UnId}"]["auth_id"] = "{}".format(ctx.author.id)
            nameandid = "ID: "+UnId+"   "+"by "+"{}".format(ctx.author.name)
            name.append(nameandid)
            url_rep = myjson.store(json.dumps(data),update=url_rep)
            url_list = myjson.store(json.dumps(name),update=url_list)
            await ctx.send("Thank you very much for the report/suggestion! :smile:")

    @commands.command()
    @commands.check(have_permissions)
    async def allreports(self, ctx):
        '''loads all reports'''
        try:
            url_list = "{}".format(os.environ.get("reported_renames"))
            name = myjson.get(url_list)
            items = json.loads(name)
            added_items = '\n'.join(items)
            try:
                out = await ctx.send("**Reports:**\n"+"```{}```".format(added_items))
            except:
                paginated_text = ctx.paginate(added_items)
                for page in paginated_text:
                    if page == paginated_text[-1]:
                        out = await ctx.send(f'```\n{page}\n```')
                        break
                    await ctx.send(f'```\n{page}\n```')
        except Exception as e:
            print("`Error: {}`".format(e))
            await ctx.send("`Error: List Not Found!`")

    @commands.command(aliases = ["inforeport"])
    @commands.check(have_permissions)
    async def inforeports(self, ctx, *,code:str = None):
        '''report infos'''
        try:
            if code == None:
                await ctx.send("`Error: Missing ID!`")
                return
            url_rep = "{}".format(os.environ.get("reported_reports"))
            data = myjson.get(url_rep)
            data = json.loads(data)
            report = data[f"{code}"]["report"]
            author = data[f"{code}"]["by"]
            author_id = data[f"{code}"]["auth_id"]
            em = discord.Embed()
            em.set_author(name = "Reports:", icon_url = "https://loading.io/spinners/recycle/lg.recycle-spinner.gif")
            em.add_field(name = "By:", value = author,inline = False)
            em.add_field(name = "Report Code:", value = code,inline = False)
            em.add_field(name = "Author ID:", value = author_id,inline = False)
            em.add_field(name = "Report:", value = report,inline = False)
            em.set_thumbnail(url = "https://i.pinimg.com/736x/0c/79/0a/0c790a5a37da132923a79f853602a36a.jpg")
            em.set_footer(text = "|Winter-Song| Report Tracker.", icon_url = self.bot.user.avatar_url)
            em.color=discord.Colour.blue()
            await ctx.send(embed = em)

        except Exception as e:
            print(e)
            await ctx.send("`Error: No such report exist!`")


def setup(bot):
	bot.add_cog(Datas(bot))
