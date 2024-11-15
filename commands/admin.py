# admin.py - Módulo responsável por comandos administrativos

import discord
import os
import signal
import asyncio
from discord.ext import commands

ADMIN_ROLE_ID = 1306412483715661844  # Variável global para o ID do cargo de admin

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() # Comando para sair do bot
    async def exit(self, ctx):
        if not any(role.id == ADMIN_ROLE_ID for role in ctx.author.roles):
            await ctx.send("Você não possui o cargo necessário para executar este comando.", delete_after=5)
            return
        await ctx.send("Saindo!")
        print("O bot foi desligado de forma forçada pelo discord! TESTETESTETESTE")

        await self.bot.close()

         # Aguarda um pouco para garantir que todas as corrotinas sejam finalizadas
        await asyncio.sleep(1)

        # Encerra o processo atual do Python, o que desativa o ambiente virtual
        os.kill(os.getpid(), signal.SIGTERM)  # Mata o processo Python


    @commands.command() # Comando só para limpar mensagens (Não vai ficar na versão final)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, user: discord.Member, limit: int = 100):
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

async def setup(bot):
    await bot.add_cog(Admin(bot))
