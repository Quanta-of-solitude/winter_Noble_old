'''
Cog by Quanta#5556
'''
import discord
from discord.ext import commands
import os
import PIL
import json
import requests
import shutil
from PIL import Image,ImageFilter,ImageDraw,ImageFont,ImageOps, ImageEnhance
import asyncio
import psycopg2

DATABASE_URL = os.environ.get("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()


class Welcomer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def have_permissions(ctx):
        return (ctx.author.guild_permissions.administrator == True or ctx.author.id == 280271578850263040 or ctx.message.author.id == 283413165381910539)




    @commands.command()
    @commands.check(have_permissions)
    async def welcomemsg(self,ctx, args:str = None, args1:str = None):
        '''set the welcome msg  Syntax w!welcomemsg msg channelid'''
        server = ctx.guild

        if args == None:
            msg = "Welcome! Have fun here <3"
        else:
            msg = args
        if args1 == None:
            channel_id = ctx.channel.id
        else:
            channel_id = args1

        check = "select exists(select * from welcomeyou where serverid='{}')".format(server.id)
        cur.execute(check)
        res = cur.fetchall()
        checked = bool(res[0][0])

        if checked is not True:
            command = (f"""INSERT INTO welcomeyou VALUES ('{server.id}','{msg}','{channel_id}','text','on','https://cdn.discordapp.com/attachments/384512083552894979/395207826684772374/bg.jpg')""")
            cur.execute(command)
            conn.commit()

            em = discord.Embed(description = "Welcome message has been set and type is text(default)")
            em.colour = discord.Colour.green()
            await ctx.send(embed = em)

        else:
            em = discord.Embed(description = "There is a welcome msg (already set), do you want to change it? Reply yes or no")
            em.colour = discord.Colour.green()
            await ctx.send(embed = em)

            def check(ctx):
                return (ctx.content == 'yes' or ctx.content == 'no' or ctx.content == 'Yes' or ctx.content == 'No')

            msge = await self.bot.wait_for('message', check=check)
            msge.content = msge.content.lower()

            if msge.content == "yes":

                command = (f"""UPDATE welcomeyou SET welcomemsg='{msg}',channelid='{channel_id}' WHERE serverid='{server.id}'""")
                cur.execute(command)
                conn.commit()

                em = discord.Embed(description = "Welcome message has been set and type is text(default)")
                em.colour = discord.Colour.green()
                await ctx.send(embed = em)
            else:
                em = discord.Embed(description = "Edit command Terminated :D")
                em.colour = discord.Colour.red()
                await ctx.send(embed = em)


    @commands.command()
    @commands.check(have_permissions)
    async def leavemsg(self,ctx, args:str = None, args1:str = None):
        '''set the leave msg  Syntax w!leavemsg msg channelid'''
        server = ctx.guild

        if args == None:
            msg = "Bye, you will be missed :frowning:"
        else:
            msg = args
        if args1 == None:
            channel_id = ctx.channel.id
        else:
            channel_id = args1

        check = "select exists(select * from leaveyou where serverid='{}')".format(server.id)
        cur.execute(check)
        res = cur.fetchall()
        checked = bool(res[0][0])

        if checked is not True:
            command = (f"""INSERT INTO leaveyou VALUES ('{server.id}','{channel_id}','{msg}','on')""")
            cur.execute(command)
            conn.commit()

            em = discord.Embed(description = "Leave message has been set")
            em.colour = discord.Colour.green()
            await ctx.send(embed = em)

        else:
            em = discord.Embed(description = "There is a leave msg (already set), do you want to change it? Reply yes or no")
            em.colour = discord.Colour.green()
            await ctx.send(embed = em)
            def check(ctx):
                return (ctx.content == 'yes' or ctx.content == 'no' or ctx.content == 'Yes' or ctx.content == 'No')

            msge = await self.bot.wait_for('message', check=check)
            msge.content = msge.content.lower()

            if msge.content == "yes":
                command = (f"""UPDATE leaveyou SET leavemsg='{msg}',channelid='{channel_id}' WHERE serverid='{server.id}'""")
                cur.execute(command)
                conn.commit()

                em = discord.Embed(description = "Leave message has been set")
                em.colour = discord.Colour.green()
                await ctx.send(embed = em)
            else:
                em = discord.Embed(description = "Edit command Terminated :D")
                em.colour = discord.Colour.red()
                await ctx.send(embed = em)



    @commands.command(aliases = ["tgwelcome", "tgwel"])
    @commands.check(have_permissions)
    async def togglewel(self,ctx, *,args:str = None):
        '''Toggle welcome or not'''

        server = ctx.guild
        check = "select exists(select * from welcomeyou where serverid='{}')".format(server.id)
        cur.execute(check)
        res = cur.fetchall()
        checked = bool(res[0][0])

        accepted = ["on", "off"]
        if args == None:
            if checked is not True:

                await ctx.send("`Welcome was not set for the this server! No actions to do here.`")
            else:
                status_now = "select welcomeswitch from welcomeyou where serverid='{}'".format(server.id)
                cur.execute(command)
                current = cur.fetchall()
                await ctx.send(f"currently welcome messages are: {current[0][0]}")
        else:
            args = args.lower()
            if args in accepted:
                if checked is True:
                    command = (f"""UPDATE welcomeyou SET welcomeswitch='{args}' WHERE serverid='{server.id}'""")
                    cur.execute(command)
                    conn.commit()
                    await ctx.send("`Welcome message set to: {}`".format(args))
                else:
                    await ctx.send("`Welcome was not set for the this server! No actions to do here.`")
            else:
                await ctx.send("`Error: Invalid Parameter, define on or off.`")

    @commands.command(aliases = ["tgleave"])
    @commands.check(have_permissions)
    async def toggleleave(self,ctx, *,args:str = None):
        '''Toggle leave or not'''
        server = ctx.guild
        check = "select exists(select * from leaveyou where serverid='{}')".format(server.id)
        cur.execute(check)
        res = cur.fetchall()
        checked = bool(res[0][0])
        accepted = ["on", "off"]
        if args == None:
            if checked is not True:

                await ctx.send("`Leave was not set for the this server! No actions to do here.`")
            else:
                status_now = "select leaveswitch from leaveyou where serverid='{}'".format(server.id)
                cur.execute(command)
                current = cur.fetchall()
                await ctx.send(f"currently leave messages are: {current[0][0]}")
        else:
            args = args.lower()
            if args in accepted:
                if checked is True:
                    command = (f"""UPDATE leaveyou SET leaveswitch='{args}' WHERE serverid='{server.id}'""")
                    cur.execute(command)
                    conn.commit()
                    await ctx.send("`Leave message set to: {}`".format(args))
                else:
                    await ctx.send("`Leave was not set for the this server! No actions to do here.`")
            else:
                await ctx.send("`Error: Invalid Parameter, define on or off.`")



    @commands.command(aliases = ["weltype"])
    @commands.check(have_permissions)
    async def settype(self,ctx, *,args:str = None):
        '''Toggle pic or text welcome'''
        server = ctx.guild
        check = "select exists(select * from welcomeyou where serverid='{}')".format(server.id)
        cur.execute(check)
        res = cur.fetchall()
        checked = bool(res[0][0])
        accepted = ["pic", "text"]
        if args == None:
            if checked is not True:

                await ctx.send("`No welcome was setup in the server, No actions to do here.`")
            else:
                status_now = "select welcometype from welcomeyou where serverid='{}'".format(server.id)
                cur.execute(command)
                current = cur.fetchall()
                await ctx.send("`Current welcome Type: {}`".format(current[0][0]))
        else:
            args = args.lower()
            if args in accepted:
                if checked is True:
                    command = (f"""UPDATE welcomeyou SET welcometype='{args}' WHERE serverid='{server.id}'""")
                    cur.execute(command)
                    conn.commit()

                    await ctx.send("`Welcome type set to: {}`".format(args))
                else:
                    await ctx.send("`No welcome was setup in the server, No actions to do here.`")
            else:
                await ctx.send("`Error: Invalid Parameter, accepted: pic or text.`")

    @commands.command(aliases = ["background"])
    @commands.check(have_permissions)
    async def setbg(self,ctx, *,args:str = None):
        '''background for welcome'''
        server = ctx.guild
        check = "select exists(select * from welcomeyou where serverid='{}')".format(server.id)
        cur.execute(check)
        res = cur.fetchall()
        checked = bool(res[0][0])
        if args == None:
            await ctx.send("`Error: Nothing provided  Note: must be a link not an attachment`")
        else:
            if checked is True:
                try:
                    response = requests.head(args)
                    resp_code = response.headers.get('content-type')
                    if "image" in resp_code:
                        link = args
                        command = (f"""UPDATE welcomeyou SET welcomelinkimage='{args}' WHERE serverid='{server.id}'""")
                        cur.execute(command)
                        conn.commit()

                        await ctx.send("`Background Image added/changed, might not show up in some cases`")
                    else:
                        await ctx.send("`Error: Not a valid image`")
                except Exception as e:
                    print(e)
                    await ctx.send("`Error: Invalid Link, also the image format must be png or jpg`")
            else:
                await ctx.send("`No welcome was setup in the server, No actions to do here.`")


    @commands.command(aliases = ["autoroler"])
    @commands.check(have_permissions)
    async def autorole(self, ctx,rolename:str = None, args:str = None):
        '''set the auto role'''
        try:
            if rolename == None or args == None:
                await ctx.send("`Error: role name not provided or Toggle?`")
                return
            role = discord.utils.find(lambda m: rolename.lower() in m.name.lower(), ctx.message.guild.roles)
            if not role:
                return await ctx.send('That role does not exist.')

            else:
                args = args.lower()

                command = (f"""INSERT INTO autoroler VALUES ('{ctx.guild.id}','{role}','{args}')""")
                cur.execute(command)
                conn.commit()

                await ctx.send("Default role set to: {}".format(role))
        except Exception as e:
            print(e)
            await ctx.send("`Error: Wrong Format!`")

    @commands.command(aliases = ["wpreview", "previewwelcome", "welpreview"])
    @commands.check(have_permissions)#to view the welcome
    async def welview(self, ctx):
        '''preview the welcome without joining'''
        try:


            is_bot = False

            server = ctx.guild
            check = "select exists(select * from welcomeyou where serverid='{}')".format(server.id)
            cur.execute(check)
            res_check = cur.fetchall()
            checked = bool(res_check[0][0])

            type_msg_image = "select welcometype,welcomemsg,welcomelinkimage from welcomeyou where serverid= '{}'".format(server.id)
            cur.execute(check_img_text)
            result = cur.fetchall()
            type_textpic = result[0][0]
            msg = result[0][1]
            imageLink = result[0][2]


            if checked is True:

                if type_textpic == "pic":
                    try:
                        try:
                            url_ser = imageLink
                            respon = requests.get(url_ser, stream=True)
                            with open('ser.png', 'wb') as ou_file:
                                shutil.copyfileobj(respon.raw, ou_file)
                            del respon
                        except Exception as e:
                            print(e)
                            url_ser = "https://cdn.discordapp.com/attachments/384512083552894979/395207826684772374/bg.jpg"
                            respon = requests.get(url_ser, stream=True)
                            with open('ser.png', 'wb') as ou_file:
                                shutil.copyfileobj(respon.raw, ou_file)
                            del respon
                        img = Image.open("profile.png")
                        new_im = Image.new("RGBA", (600,200))
                        bg_w, bg_h = new_im.size
                        other = Image.open("ser.png")
                        other = other.resize((600, 200), PIL.Image.ANTIALIAS)
                        other.save('resized_bg.jpg')
                        others = Image.open("resized_bg.jpg")
                        brightness = 0.5
                        enhancer = ImageEnhance.Brightness(others)
                        others = enhancer.enhance(brightness)
                        new_im.paste(others,(0,0))
                        img.thumbnail((75,75))
                        new_im.paste(img,(42,65))
                        font1 = ImageFont.truetype('arialbd.ttf', 25)
                        font2 = ImageFont.truetype('Pacifico.ttf',20)
                        font3 = ImageFont.truetype('Tabitha.ttf', 22)
                        xoff, yoff = (10,5)
                        d = ImageDraw.Draw(new_im)
                        d.text((149, 31),"Welcome!", fill="white",font = font1)
                        t = ImageDraw.Draw(new_im)
                        t.text((137, 63),"Noble#5556", fill="white",font = font3)
                        m = ImageDraw.Draw(new_im)
                        print(len(msg))
                        if len(msg)>50:
                            msg = "Have Fun and Enjoy your time in here!"

                        m.text((136, 80),"{}".format(msg), fill="white",font = font2)
                        kk = ImageDraw.Draw(new_im)
                        kk.text((137, 109),"Member Number: 1", fill="white",font = font2)
                        if is_bot == True:
                            is_bot = "Yes"
                        else:
                            is_bot = "No"
                        bb = ImageDraw.Draw(new_im)
                        bb.text((136, 134),"Bot: {}".format(is_bot), fill="white",font = font2)
                        new_im.save("welcome_test.png")
                        await ctx.send(content = "**This is the preview of the welcome you set.**",file=discord.File('welcome_test.png'))
                    except Exception as e:
                        print(e)
                        await ctx.send("The image link might be invalid (not a valid .png/.jpg link) :sweat_smile:")

                if type_textpic == "text":

                    await ctx.send("`This is a preview of the welcome you set.`\n\n{}".format(msg)+"\n\n**Member:** <@385681784614027265>"+"\n**Server:** **{}**".format(ctx.guild.name)+"\n**Member No:** 1"+"\n**Bot:** {}".format(is_bot))
            else:
                await ctx.send("You haven't set a welcome message using me yet :smile:")
        except Exception as e:
            print(e)

    @commands.command()#owner command only
    async def preview(self, ctx, *,server:str = None):
        '''to preview welcome on any server'''
        if ctx.author.id == 280271578850263040:
            if server == None:
                await ctx.send("You missed to give an id!")
                return
            try:

                is_bot = False

                serrv = self.bot.get_guild(int(server))
                server = serrv
                check = "select exists(select * from welcomeyou where serverid='{}')".format(server.id)
                cur.execute(check)
                res_check = cur.fetchall()
                checked = bool(res_check[0][0])

                type_msg_image = "select welcometype,welcomemsg,welcomelinkimage from welcomeyou where serverid= '{}'".format(server.id)
                cur.execute(check_img_text)
                result = cur.fetchall()
                type_textpic = result[0][0]
                msg = result[0][1]
                imageLink = result[0][2]


                if checked is True:

                    if type_textpic == "pic":

                        try:
                            try:
                                url_ser = imageLink
                                respon = requests.get(url_ser, stream=True)
                                with open('ser.png', 'wb') as ou_file:
                                    shutil.copyfileobj(respon.raw, ou_file)
                                del respon
                            except Exception as e:
                                print(e)
                                url_ser = "https://cdn.discordapp.com/attachments/384512083552894979/395207826684772374/bg.jpg"
                                respon = requests.get(url_ser, stream=True)
                                with open('ser.png', 'wb') as ou_file:
                                    shutil.copyfileobj(respon.raw, ou_file)
                                del respon
                            img = Image.open("profile.png")
                            new_im = Image.new("RGBA", (600,200))
                            bg_w, bg_h = new_im.size
                            other = Image.open("ser.png")
                            other = other.resize((600, 200), PIL.Image.ANTIALIAS)
                            other.save('resized_bg.jpg')
                            others = Image.open("resized_bg.jpg")
                            brightness = 0.5
                            enhancer = ImageEnhance.Brightness(others)
                            others = enhancer.enhance(brightness)
                            new_im.paste(others,(0,0))
                            img.thumbnail((75,75))
                            new_im.paste(img,(42,65))
                            font1 = ImageFont.truetype('arialbd.ttf', 25)
                            font2 = ImageFont.truetype('Pacifico.ttf',20)
                            font3 = ImageFont.truetype('Tabitha.ttf', 22)
                            xoff, yoff = (10,5)
                            d = ImageDraw.Draw(new_im)
                            d.text((149, 31),"Welcome!", fill="white",font = font1)
                            t = ImageDraw.Draw(new_im)
                            t.text((137, 63),"Noble#5556", fill="white",font = font3)
                            m = ImageDraw.Draw(new_im)
                            print(len(msg))
                            if len(msg)>50:
                                msg = "Have Fun and Enjoy your time in here!"

                            m.text((136, 80),"{}".format(msg), fill="white",font = font2)
                            kk = ImageDraw.Draw(new_im)
                            kk.text((137, 109),"Member Number: 1", fill="white",font = font2)
                            if is_bot == True:
                                is_bot = "Yes"
                            else:
                                is_bot = "No"
                            bb = ImageDraw.Draw(new_im)
                            bb.text((136, 134),"Bot: {}".format(is_bot), fill="white",font = font2)
                            new_im.save("welcome_test.png")
                            await ctx.send(content = f"**The Server is {serrv.name}**",file=discord.File('welcome_test.png'))
                        except Exception as e:
                            print(e)
                            await ctx.send("The image link might be invalid (not a valid .png/.jpg link) :sweat_smile:")

                    if type_textpic == "text":

                        await ctx.send("`This is a preview of the welcome they set.`\n\n{}".format(msg)+"\n\n**Member:** <@385681784614027265>"+"\n**Server:** **{}**".format(serrv.name)+"\n**Member No:** 1"+"\n**Bot:** {}".format(is_bot))
                else:
                    await ctx.send("They haven't set a welcome message using me yet :smile:")
            except Exception as e:
                print(e)

#Events========================================================================================================================================
    async def on_member_join(self,member):
        '''welcome!'''
        try:
            server = member.guild
            user = member
            is_bot = user.bot

            check = "select exists(select * from welcomeyou where serverid='{}')".format(server.id)
            cur.execute(check)
            res_check = cur.fetchall()
            checked = bool(res_check[0][0])

            type_msg_image = "select welcometype,welcomemsg,welcomelinkimage,welcomeswitch,channelid from welcomeyou where serverid= '{}'".format(server.id)
            cur.execute(check_img_text)
            result = cur.fetchall()
            type_textpic = result[0][0]
            msg = result[0][1]
            imageLink = result[0][2]
            on_off = result[0][3]
            chan_id = result[0][4]

            check_exist = "select exists(select * from autoroler where serverid='{}')".format(server.id)
            cur.execute(check_exist)
            res_role = cur.fetchall()
            check_role = bool(res_role[0][0])

            type_autorole = "select roleidname,roleswitch from autoroler where serverid= '{}'".format(server.id)
            cur.execute(check_img_text)
            result_role = cur.fetchall()
            rolerName = result_role[0][0]
            roleswitch = result_role[0][1]

            member_number = sorted(server.members, key=lambda m: m.joined_at).index(user) + 1

            if checked is True and on_off == "on" and type_textpic == "pic":

                #await channel.send("{}".format(msg)+"\n\n**Member:** {0.mention}".format(member)+"\n**Server:** **{}**".format(server.name)+"\n**Member No:** {}".format(member_number)+"\n**Bot:** {}".format(is_bot))
                channel_id = chan_id
                msg = msg
                channel = self.bot.get_channel(int(channel_id))
                url = '{}'.format(member.avatar_url)
            #    print(url)
                response = requests.get(url, stream=True)
                with open('img.png', 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                del response
                #url_ser = '{}'.format(server.icon_url_as(format = 'png'))
                #print(url_ser)
                try:
                    url_ser = imageLink
                    respon = requests.get(url_ser, stream=True)
                    with open('ser.png', 'wb') as ou_file:
                        shutil.copyfileobj(respon.raw, ou_file)
                    del respon

                except Exception as e:
                    print(e)
                    url_ser = "https://cdn.discordapp.com/attachments/384512083552894979/395207826684772374/bg.jpg"
                    respon = requests.get(url_ser, stream=True)
                    with open('ser.png', 'wb') as ou_file:
                        shutil.copyfileobj(respon.raw, ou_file)
                    del respon
                img = Image.open("img.png")
                new_im = Image.new("RGBA", (600,200))
                bg_w, bg_h = new_im.size
                other = Image.open("ser.png")
                other = other.resize((600, 200), PIL.Image.ANTIALIAS)
                other.save('resized_bg.jpg')
                others = Image.open("resized_bg.jpg")
                brightness = 0.5
                enhancer = ImageEnhance.Brightness(others)
                others = enhancer.enhance(brightness)
                new_im.paste(others,(0,0))
                img.thumbnail((75,75))
                new_im.paste(img,(42,65))
                font1 = ImageFont.truetype('arialbd.ttf', 25)
                font2 = ImageFont.truetype('Pacifico.ttf',20)
                font3 = ImageFont.truetype('Tabitha.ttf', 22)
                xoff, yoff = (10,5)
                d = ImageDraw.Draw(new_im)
                d.text((149, 31),"Welcome!", fill="white",font = font1)
                t = ImageDraw.Draw(new_im)
                t.text((137, 63),"{}".format(member), fill="white",font = font3)
                m = ImageDraw.Draw(new_im)
                print(len(msg))
                if len(msg)>50:
                    msg = "Have Fun and Enjoy your time in here!"

                m.text((136, 80),"{}".format(msg), fill="white",font = font2)
                kk = ImageDraw.Draw(new_im)
                kk.text((137, 109),"Member Number: {}".format(member_number), fill="white",font = font2)
                if is_bot == True:
                    is_bot = "Yes"
                else:
                    is_bot = "No"
                bb = ImageDraw.Draw(new_im)
                bb.text((136, 134),"Bot: {}".format(is_bot), fill="white",font = font2)
                new_im.save("welcome_test.png")
                await channel.send(content = "{0.mention}".format(member),file=discord.File('welcome_test.png'))

                try:

                    if check_role is True and rolerName is not None and roleswitch == "on":

                        rolename = rolerName
                        role = discord.utils.find(lambda m: rolename.lower() in m.name.lower(), server.roles)
                        await member.add_roles(role)
                except Exception as e:
                    pass

            elif checked is True and on_off == "on" and type_textpic == "text":
            #elif "{}".format(server.id) in data_message and data_toggle["{}".format(server.id)]["set_welcome"] == "on" and data_type["{}".format(server.id)]["msg_type"] == "text" or not data_type["{}".format(server.id)]:
                channel_id = chan_id
                msg = msg
                channel = self.bot.get_channel(int(channel_id))
                await channel.send("{}".format(msg)+"\n\n**Member:** {0.mention}".format(member)+"\n**Server:** **{}**".format(server.name)+"\n**Member No:** {}".format(member_number)+"\n**Bot:** {}".format(is_bot))

                try:
                    if check_role is True and rolerName is not None and roleswitch == "on":

                        rolename = rolerName
                        role = discord.utils.find(lambda m: rolename.lower() in m.name.lower(), server.roles)
                        await member.add_roles(role)
                except Exception as e:
                    pass

        except Exception as e:
            print(e)
            try:
                if checked is True and on_off == "on" and type_textpic == "pic":
                ##if "{}".format(server.id) in data_message and data_toggle["{}".format(server.id)]["set_welcome"] == "on" and data_type["{}".format(server.id)]["msg_type"] == "pic":
                    channel_id = chan_id
                    channel = self.bot.get_channel(int(channel_id))
                    msg = msg
                    await channel.send("`Error encountered while creating image, please check the format of the bg provided(png, jpg).`\n")
                    await channel.send("{}".format(msg)+"\n\n**Member:** {0.mention}".format(member)+"\n**Server:** **{}**".format(server.name)+"\n**Member No:** {}".format(member_number)+"\n**Bot:** {}".format(is_bot))
            except Exception as erre:
                print(erre)

    async def on_member_remove(self,member):
        '''Leave!'''
        try:
            server = member.guild
            user = member
            is_bot = user.bot
            url_toggle = self.toggle_url2()
            url_message = self.load_url2()
            data_toggle = myjson.get(url_toggle)
            data_toggle = json.loads(data_toggle)
            data_message = myjson.get(url_message)
            data_message = json.loads(data_message)

            check = "select exists(select * from leaveyou where serverid='{}')".format(server.id)
            cur.execute(check)
            res_check = cur.fetchall()
            checked = bool(res_check[0][0])

            type_msg_image = "select leaveswitch,leavemsg,channelid from leaveyou where serverid= '{}'".format(server.id)
            cur.execute(check_img_text)
            result = cur.fetchall()
            toggle_val = result[0][0]
            msg = result[0][1]
            chan_id = result[0][2]

            channel_chan_id
            channel = self.bot.get_channel(int(channel_id))
            #member_number = sorted(server.members, key=lambda m: m.joined_at).index(user) + 1
            if checked is True and toggle_val == "on":

                await channel.send("{}".format(msg)+"\n\n**Member:** {}".format(member.name)+"\n**Server:** **{}**".format(server.name)+"\n**Bot:** {}".format(is_bot)+"\n:wave:")
        except Exception as e:
            #print(e)
            pass

    async def on_guild_join(self, guild):
        try:
            server = guild
            channel = server.text_channels[0]
            msg = "**Thank you for adding me! :slight_smile:\nI am winter-song, and if by mistake I wrote this on an unwanted channel, please forgive me**:sweat_smile:\nTo get started, use **w!help** and you will see all my commands! :dancer:\nYou can also check the website: https://winter-song-web.herokuapp.com/ I hope it's **working** :smile:"
            await channel.send(msg)
        except Exception as e:
            pass




def setup(bot):
	bot.add_cog(Welcomer(bot))
