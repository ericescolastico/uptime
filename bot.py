# bot.py - Arquivo principal para rodar o bot

import os
import discord
import asyncio

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('discord.env', override=True) # Carrega arquivo de chaves

intents = discord.Intents.all() # Permissões
intents.message_content = True
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)
discord_token = os.getenv('DISCORD_KEY') # Carrega API KEY do Discord

# Carregar módulos (cogs)
async def load_extensions():
    for extension in ['commands.livroponto', 'commands.admin', 'commands.utilitarios']:
        await bot.load_extension(extension)

# Carrega as extensões e executa o bot
async def main():
    async with bot:
        await load_extensions()
        await bot.start(discord_token)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("O bot foi interrompido manualmente.")