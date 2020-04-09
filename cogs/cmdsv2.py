'''
Anybody can add commands, and edit them, can put pictures or texts but not both.
PS: if using pics , do not use short links, instead use those with extension. <Just a suggestion

Cog By Noble#5556

'''
import os
import re
import json
import discord
import requests
from discord.ext import commands

import psycopg2

DATABASE_URL = os.environ.get("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

class cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def is_owner(ctx):
        return (ctx.author.id == 280271578850263040 or ctx.author.id == 283413165381910539)



    @commands.command()
    async def cmdadd(self, ctx,*,args:str = None):
        '''add commands'''

        if args == None:
            await ctx.send("`Missing command.`")
            return
        else:
            check = "select exists(select * from cmds where authorid='{}')".format(ctx.author.id)
            cur.execute(check)
            res = cur.fetchall()
            checked = bool(res[0][0])
            args = args.lower()
            if checked is not True:
                command= (f"""INSERT INTO cmds VALUES('{ctx.author.id}','{ctx.author}','{args}')""")
                cur.execute(command)
                conn.commit()
                em = discord.Embed(description = "Your command has been added :)")
                em.colour = discord.Colour.green()
                await ctx.send(embed = em)
            else:
                find = (f"""select cmd from cmds where authorid= '{ctx.author.id}'""")
                cur.execute(find)
                result = cur.fetchall()
                cmd_y = result[0][0]

                em = discord.Embed(description = f"You have already added a command that says:`{cmd_y}`. Do you want to change it?")
                em.colour = discord.Colour.green()
                await ctx.send(embed = em)
                def check(ctx):
                    return (ctx.content == 'yes' or ctx.content == 'no' or ctx.content == 'Yes' or ctx.content == 'No')
                msg = await self.bot.wait_for('message', check=check)
                msg.content = msg.content.lower()

                if msg.content == "yes" and checked is True:
                    command = (f"""UPDATE cmds SET cmd='{args}' WHERE authorid= '{ctx.author.id}'""")
                    cur.execute(command)
                    conn.commit()
                    em = discord.Embed(description = "The Command has been edited :)")
                    em.colour = discord.Colour.green()
                    await ctx.send(embed = em)
                else:
                    em = discord.Embed(description = "Process exited")
                    em.colour = discord.Colour.red()
                    await ctx.send(embed = em)

    @commands.command()
    async def cmd(self, ctx, *,args:str = None):
        '''get the command'''
        url = self.load_url()
        if args == None:
            author_id = ctx.author.id
        else:
            author_id = args

            check = "select exists(select * from cmds where authorid= '{}')".format(author_id)
            cur.execute(check)
            res = cur.fetchall()
            checked = bool(res[0][0])
            if checked is True:

                datas = (f"""select cmd,authroname from cmds where authorid= '{author_id}'""")
                cur.execute(datas)
                result_item = cur.fetchall()
                cmdData = result_item[0][0]
                nameAuth = result_item[0][1]

                try:

                    url = cmdData
                    response = requests.head(url)
                    resp_code = response.headers.get('content-type')
                    #extentions = [".gif",".jpg",".webp",".png"]
                    if "image" in resp_code:
                        em = discord.Embed()
                        em.set_image(url = url)
                        em.set_footer(text = "Added by {}".format(nameAuth))
                        await ctx.send(embed = em)
                    else:
                        em = discord.Embed(description = url)
                        em.colour = discord.Colour.blue()
                        em.set_footer(text = "Added by {}".format(nameAuth))
                        await ctx.send(embed = em)
                except Exception as e:
                    await ctx.send("`The provided custom had an error, link`")
            else:
                await ctx.send("`No command was added.`")




    @commands.command()
    async def allcmds(self, ctx):
        '''list of all commands added'''
        datas = ("""select cmd from cmds""")
        cur.execute(datas)
        results = cur.fetchall()
        talks = []
        for i in results:
            talks.append(i[0])

        key = '\n'.join(talks[:20])
        current_count = len(talks)
        command_list = "```py\nList will show only upto (20) commands, currently ({}):\n\n{}\n```".format(current_count,key)
        await ctx.send(command_list)

    '''@commands.command()
    @commands.check(is_owner)
    async def delcmd(self, ctx, *,args):

        try:
            url = self.load_url()
            data = myjson.get(url)
            data = json.loads(data)
            args = args.lower()
            if args in data:
                em = discord.Embed(description = "**{}** has been removed ,which was added by **{}**".format(args, data["{}".format(args)]["added_by"]))
                em.colour = discord.Colour.green()
                data.pop('{}'.format(args), None)
                url = myjson.store(json.dumps(data),update=url)
                await ctx.send(embed = em)
            else:
                em = discord.Embed(description = "No such command exists.")
                em.colour = discord.Colour.red()
                await ctx.send(embed =em)
        except Exception as e:
            #print(e)
            await ctx.send("`Error: 'key'`")'''


def setup(bot):
	bot.add_cog(cmds(bot))
