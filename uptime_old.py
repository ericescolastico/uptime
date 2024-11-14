import os  ## Biblioteca utilizada para importar secrets
import datetime #Biblioteca para utilizar tempos e datas

import discord

from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime

load_dotenv('discord.env', override=True) #Carrega arquivo de chaves

intents = discord.Intents.all() # Permissões
intents.message_content=True
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)
discord_token = os.getenv('DISCORD_KEY')    #Carrega API KEY do Discord

CARGO_ID = 1121835820723228743  # Variável global para o ID do cargo específico
ADMIN_ROLE_ID = 1306412483715661844  # Variável global para o ID do cargo de admin
CHANNEL_ID = 1137841014657265684  # Variável global para o ID do canal específico

@bot.event
async def on_presence_update(before, after):
    # Definindo data e hora no início da função para garantir que sempre estejam disponíveis
    current_time = datetime.now()
    date = current_time.strftime("%Y-%m-%d")
    time = current_time.strftime("%H:%M:%S")
    has_specific_role = any(role.id == CARGO_ID for role in after.roles)

    # Verifica se o usuário possui o cargo específico
    if has_specific_role:
        # Checa se o usuário foi de offline para online, idle, ou dnd
        if before.status == discord.Status.offline and after.status in {discord.Status.online, discord.Status.idle, discord.Status.dnd}:
            channel = await bot.fetch_channel(CHANNEL_ID)
            await channel.send(f"{before.name} ficou online em {date} no seguinte horário {time}")
        
        # Checa se o usuário foi de online, idle, ou dnd para offline
        elif before.status in {discord.Status.online, discord.Status.idle, discord.Status.dnd} and after.status == discord.Status.offline:
            channel = await bot.fetch_channel(CHANNEL_ID)
            await channel.send(f"{before.name} ficou offline em {date} no seguinte horário {time}")
    
    else: # Usuário não possui o cargo 
        print(f"{after.name} alterou o status, mas não possui o cargo requerido.")


############## Somente utilitários eventos de saida e entrada de bot e etc
@bot.event #Evento de prontidão (Imprime no terminal a entrada)
async def on_ready():
  print(f"O bot está pronto! {bot.user}")

@bot.command() #Comando para sair do bot
async def exit(ctx):
    if not any(role.id == ADMIN_ROLE_ID for role in ctx.author.roles):
        await ctx.send("Você não possui o cargo necessário para executar este comando.", delete_after=5)
        return
    await ctx.send("Saindo!")
    await bot.close()
@bot.event #Evento de Saída (Imprime no terminal a saída)
async def on_disconnect(): 
    print(f"O bot está desligado! {bot.user}")

@bot.command() #Comando só para limpar mensagens (Não vai ficar na versão final)
@commands.has_permissions(manage_messages=True)
async def purge(ctx, user: discord.Member, limit: int = 100):
    if not any(role.id == ADMIN_ROLE_ID for role in ctx.author.roles):
        await ctx.send("Você não possui o cargo necessário para executar este comando.", delete_after=5)
        return
    """Apaga mensagens de um determinado usuário."""
    def is_user(msg):
        return msg.author == user

    try:
        deleted = await ctx.channel.purge(limit=limit, check=is_user)  # Apaga as mensagens que correspondem ao usuário
        await ctx.send(f'Apagadas {len(deleted)} mensagens de {user.mention}.', delete_after=5)  # Mensagem de confirmação
    except discord.Forbidden:
        await ctx.send("Eu não tenho permissão para apagar mensagens nesse canal.")
    except discord.HTTPException as e:
        await ctx.send(f"Ocorreu um erro ao tentar apagar mensagens: {e}")



bot.run(discord_token)
