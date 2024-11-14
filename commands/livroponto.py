# livroponto.py - Módulo responsável pela verificação de status e integração com Google Sheets

import discord
from discord.ext import commands
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Variáveis globais
CARGO_ID = 1121835820723228743  # ID do cargo específico
CHANNEL_ID = 1137841014657265684  # ID do canal específico

# Configuração do Google Sheets
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
credentials = ServiceAccountCredentials.from_json_keyfile_name("keys/discord-bot-439701-9478347fa2aa.json", scope)
client = gspread.authorize(credentials)
sheet = client.open("Livro de Ponto Discord").sheet1

class LivroPonto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        # Definindo data e hora no início da função para garantir que sempre estejam disponíveis
        current_time = datetime.now()
        date = current_time.strftime("%Y-%m-%d")
        time = current_time.strftime("%H:%M:%S")
        has_specific_role = any(role.id == CARGO_ID for role in after.roles)

        # Verifica se o usuário possui o cargo específico
        if has_specific_role:
            # Checa se o usuário foi de offline para online, idle, ou dnd
            if before.status == discord.Status.offline and after.status in {discord.Status.online, discord.Status.idle, discord.Status.dnd}:
                channel = await self.bot.fetch_channel(CHANNEL_ID)
                await channel.send(f"{before.name} ficou online em {date} no seguinte horário {time}")
                sheet.append_row([before.name, before.id, "ENTROU", date, time])
            
            # Checa se o usuário foi de online, idle, ou dnd para offline
            elif before.status in {discord.Status.online, discord.Status.idle, discord.Status.dnd} and after.status == discord.Status.offline:
                channel = await self.bot.fetch_channel(CHANNEL_ID)
                await channel.send(f"{before.name} ficou offline em {date} no seguinte horário {time}")
                sheet.append_row([before.name, before.id, "SAIU", date, time])
        
        else:  # Usuário não possui o cargo
            print(f"{after.name} alterou o status, mas não possui o cargo requerido.")

async def setup(bot):
    await bot.add_cog(LivroPonto(bot))
