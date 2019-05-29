'''
TAKEN FROM COG EXAMPLES.
'''

from discord.ext import commands


class Ownes(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def is_owner(ctx):
        return (ctx.author.id == 280271578850263040 or ctx.author.id == 283413165381910539)
    @commands.command(name='load', hidden=True)
    @commands.check(is_owner)
    async def loadin(self, ctx, *, cog: str):
        """load module using cogs.module"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='unload', hidden=True)
    @commands.check(is_owner)
    async def unloadin(self, ctx, *, cog: str):
        """Unload using cogs.module"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='reload', hidden=True)
    @commands.check(is_owner)
    async def reloadin(self, ctx, *, cog: str):
        """reload module , use cogs.module"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


def setup(bot):
    bot.add_cog(Ownes(bot))
