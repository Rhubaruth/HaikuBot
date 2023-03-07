import discord
from discord.ext import commands, tasks


import random
import datetime as dt
import haiku


intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

GUILD_ARUGULA = 1081598295824158842
CHANNEL_BOT = 1081598357786603581

''' !!! ALL TIMES ARE IN UTC -> +0:00 '''
utc = dt.timezone.utc
HAIKU_TIMES = [
    dt.time(hour=8,  minute=30, tzinfo=utc),
    dt.time(hour=11, minute=00, tzinfo=utc),
    dt.time(hour=15, minute=15, tzinfo=utc),
    dt.time(hour=19, minute=00, tzinfo=utc)
    ]


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print("------")
    await bot.add_cog(HaikuCog(bot))
    cog = bot.get_cog("HaikuCog")
    await cog.cog_load()


@bot.command(name='hello', help='Will greet you')
async def greet(ctx: discord.ext.commands.context.Context):
    server = ctx.message.guild
    senders_name = ctx.message.author.name
    senders_nick = ctx.message.author.nick
    await ctx.send(f'Hello {senders_nick if senders_nick is not None else senders_name}')
    # print(f'{server}, {type(ctx)}')


@bot.command(name='commands', help='Will help you probably')
async def help_cogs(ctx, cog_name=None):
    if cog_name is None:
        await ctx.send('Enter a cog name')
        return

    cog = bot.get_cog(cog_name + "Cog")
    if cog is None:
        await ctx.send(f'Cog {cog_name} doesnt exist')
        return
    cog_commands = cog.get_commands()
    if len(cog_commands) == 0:
        await ctx.send('No available commands')
        return
    for c in cog_commands:
        await ctx.send(c.name)


async def random_members(guild, n):
    member_count = guild.member_count
    rand_nums = []
    while len(rand_nums) < int(n) and len(rand_nums) < member_count:
        rand = random.randint(0, member_count-1)
        if rand not in rand_nums:
            rand_nums += [rand]

    members = [guild.members[rand_n] for rand_n in rand_nums]
    print(members)
    return members


class HaikuCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_task.start()
        print("Cog Initialized")

    def cog_unload(self):
        self.my_task.cancel()

    @tasks.loop(time=HAIKU_TIMES)   # scheduling task runs daily
    async def my_task(self):
        bot.get_guild(GUILD_ARUGULA)
        channel = bot.get_channel(CHANNEL_BOT)
        h = haiku.create_haiku()
        h = '\n'.join(h)
        await channel.send(h)
