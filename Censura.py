import discord
from discord.ext import commands

# Token do seu bot do Discord
TOKEN = 'seu_token_aqui'

# Lista de palavras proibidas
palavras_proibidas = ['palavra1', 'palavra2', 'outra_palavra']

# Inicialização do bot
bot = commands.Bot(command_prefix='!')

# Evento de inicialização do bot
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Evento de monitoramento de mensagens
@bot.event
async def on_message(message):
    # Verifica se a mensagem vem de um usuário e não do próprio bot
    if message.author == bot.user:
        return

    content = message.content.lower()

    # Verifica se a mensagem contém palavras proibidas
    for palavra in palavras_proibidas:
        if palavra in content:
            # Censura a mensagem
            await message.delete()

            # Bane o usuário
            await message.author.ban(reason='Mensagem contém palavra proibida.')
            await message.channel.send(f'{message.author.mention} foi banido por enviar mensagem com conteúdo proibido.')

            return

    # Passa a mensagem para outros comandos se não houver palavras proibidas
    await bot.process_commands(message)

# Comando de exemplo
@bot.command()
async def hello(ctx):
    await ctx.send('Olá!')

# Executa o bot
bot.run(TOKEN)
