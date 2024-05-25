import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user.name} olarak giriş yapıldı.')
@bot.command()
async def öneri(ctx):
    ctx.send("cam atıklara atabilirsiniz :D ")
@bot.command()
async def cam(ctx):
    with open('IMG-4280821703404384188.webp', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
# Botunuzu çalıştırmak için tokeninizi buraya girin
bot.run('')
