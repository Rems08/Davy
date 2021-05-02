import json
# on importe le module discord.py
import discord
import requests
from random import*
from discord.utils import get
# ajouter un composant de discord.py
from discord.ext import commands
import time #On importe le module time pour la commande sleep

class creationTournois:
    '''
    Cette classe permettra de créer un tournois de A à Z
    '''
    def __init__(self):
        print("Création d'un tournois")
        self.nom = "Test_nom"
        self.numberTeam = 5
    async def test(ctx, nomDuTournois):
        mon_tournois = {
            "nom": nomDuTournois
        }
        phraseBot = "Votre tournoi s'appelle: " + mon_tournois["nom"]
        await ctx.send(phraseBot)

creationTournois()