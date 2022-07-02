from pickle import PicklingError
from pydoc import describe
import discord
import config
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from mcstatus import JavaServer as MinecraftServer
#from automatic import st
from config import *

prefix = config.prefix
token = config.token


bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

slash = SlashCommand(bot,sync_commands=True)


@bot.event
async def on_connect():
    print(f'Login as {bot.user.name}\nhttps://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=2147483648&scope=bot%20applications.commands')
    await bot.change_presence(activity=discord.Streaming(name= f"마인크래프트 서버", url="https://www.twitch.tv/whitehole"))






@slash.slash(
    name="mcinfo",
    description="마인크래프트 서버의 상세 정보를 확인합니다."
    )
async def mc_server_info(ctx,서버주소 : str):
    try:
        mc_server = MinecraftServer.lookup(서버주소)
        mc_server_status = mc_server.status()
        



        embed = discord.Embed(title = f"{서버주소}의 정보 입니다.",color=0x5cb85c)
        embed.add_field(name='주소', value=f"`{mc_server.address.host}`", inline=True)
        embed.add_field(name='포트', value=f"`{mc_server.address.port}`", inline=True)
        embed.add_field(name='버전', value=f"`{mc_server_status.version.name}`", inline=True)
        embed.add_field(name='핑', value=f"`{mc_server_status.latency}ms`", inline=True)
        embed.add_field(name='플레이어', value=f"`{mc_server_status.players.online}/{mc_server_status.players.max}`", inline=True)
        embed.add_field(name='설명', value=f"`{mc_server_status.description}`", inline=True)
        await ctx.send(embed=embed)
    except Exception as error:    
        await ctx.send(embed=discord.Embed(title=f"❌오류가 발생하였습니다❌",description = "잘못된 주소 이거나 알수없는 문제가 발생하였습니다.",color = discord.Colour.dark_red()))
        print(error)




bot.run(token)       