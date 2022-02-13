#!/usr/bin/python3 -u

# inrahbot.py
import os
import discord
import random

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', help_command=None)

@bot.command(name='inrahbot')
async def get_card(ctx):
    flair_text = ["Werfe die Knochen...", "Würfle das Schicksal...", "Befrage die Geister...", "Blicke in die Kristallkugel...", "Lese in den Teeblättern...", "Deute die Träume...", "Deute die Flammen...", "Finde die Wasserläufe...", "Lese in den Al'Anfanischen Prophezeiungen...", "Gehe auf Visionssuche...", "Deute die heiligen Rollen...", "Deute die Zahlen...", "Betrachte den Vogelflug..."]
    await ctx.send(random.choice(flair_text))
    card = random.randint(1,121)
    with open('Karten/' + str(card).zfill(3) + '.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    with open('Texte/' + str(card).zfill(3) + '.txt', 'r') as f:
        await ctx.send(f.read())

@bot.command()
async def help(ctx):
    response = "Dieser bot generiert eine zufällige Inrah-Karte und zeigt diese und die dazugehörige Beschreibung an. Command: `!inrahbot`"
    await ctx.send(response)

bot.run(TOKEN)