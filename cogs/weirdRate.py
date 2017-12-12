'''
Weird Rating - Cog by Quanta (N)
'''

import os
import discord
import json
from discord.ext import commands
from cleverwrap import CleverWrap
from matplotlib import pyplot as plt
from matplotlib import style
matplotlib.use('Agg')
import random

class Rating:

    def __init__(self, bot):
        self.bot = bot

    def rand_x1(self):
        random_x1 = random.sample(range(0,10), 5)
        return random_x1

    def rand_y1(self):
        random_y1 = random.sample(range(0,10), 5)
        return random_y1

    def rand_x2(self):
        random_x2 = random.sample(range(1,8), 5)
        return random_x2

    def rand_y2(self):
        random_y2 = random.sample(range(1,8), 5)
        return random_y2

    def plotting(self, x, y, x1, y1):
        plt.plot(x,y,linewidth=3)
        plt.plot(x1,y1,linewidth=2)
        plt.title('Rating')
        plt.ylabel('Weirdness')
        plt.xlabel('Personality')
        return plt

    @commands.command()
    async def rate(self,ctx):
        x1 = self.rand_x1()
        y1 = self.rand_y1()
        x2 = self.rand_x2()
        y2 = self.rand_y2()
        graph_made = self.plotting(x1,y1,x2,y2)
        graph_made.savefig("weird_rating.jpg")
        await ctx.send(content = "**Here is your Weird Rating:**",file=discord.File("weird_rating.jpg"))





def setup(bot):
	bot.add_cog(Rating(bot))
