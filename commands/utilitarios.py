# utilitarios.py - Módulo responsável por eventos utilitários do bot

from discord.ext import commands

class Utilitarios(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() # Evento de prontidão (Imprime no terminal a entrada)
    async def on_ready(self):
        print(f"O bot está pronto! {self.bot.user}")

    @commands.Cog.listener() # Evento de Saída (Imprime no terminal a saída)
    async def on_disconnect(self):
        print(f"O bot está desligado! {self.bot.user}")

async def setup(bot):
    await bot.add_cog(Utilitarios(bot))
