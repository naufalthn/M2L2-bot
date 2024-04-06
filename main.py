import imp
import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
                    picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_fox_image_url():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('fox')
async def fox(ctx):
    '''Setelah kita memanggil perintah fox (fox), program akan memanggil fungsi get_fox_image_url'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)

organic = [
     'sisa makanan',
     'bahan kimia',
     'daun',
     'botol kertas',
     'kotoran hewan',
     'minyak bekas',
     'kertas', 
     'kayu'
     'batu'
     'minyak bumi'
]
anorganic = [
     'kaca',
     'stereofoam',
     'plastik',
     'barang elektronik',
     'kaleng alumunium',
     'besi',
     'ban bekas',
     'karet'
]

@bot.command()
async def sampah(ctx):
     await ctx.send('Masukkan jenis sampah yang ingin kamu ketahui: ')
     msg = await bot.wait_for('message')
     if msg.content in organic:
          await ctx.send('Buang di tempat sampah ORGANIK😊')
     elif msg.content in anorganic:
          await ctx.send('Buang di tempat sampah ANORGANIK😊')
     else:
          await ctx.send('Maaf kami tidak menemukan barang itu🙏')



bot.run("MTIxODQxNjQ4NTU1MTA1MDk0Mw.GJaJ1l.lYLmwii8BRoxM1DNYD6kFNAxzaTr_iFM3_vPY8")