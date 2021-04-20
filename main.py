import json
# on importe le module discord.py
import discord
import requests
from random import*
from discord.utils import get
# ajouter un composant de discord.py
from discord.ext import commands
import time #On importe le module time pour la commande sleep
global piedsTeenWolf #Initialisation d'une variable globale qui va compter à partir de cette dernière
piedsTeenWolf = 0
global administrateur
administrateur = "<@&596072853116420112>" #Identifiant du grade admin sur Cyber-Sport
# créer le bot
bot = commands.Bot(command_prefix='!') #Permettra au bot de savoir quand est-ce qu'on lui parle grâce au str de command_prefix
client = discord.Client()
bot.remove_command('help') #Supprime la commande help afin de créer note propre commande

# détecter quand le bot est pret ("allumé")
@bot.event
async def on_ready():
    print("Bot pret")
    await bot.change_presence(status=discord.Status.online,
            activity=discord.Game("!help #Rems"))
            
# créer la commande !regles
@bot.command()
async def regles(ctx):
    '''Cette commande permet d'afficher les règles du serveur Cyber-Sport'''
    await ctx.send(f"Voir le salon <#789107176483979304> pour plus d'information concernant les règles.")

#Créer la commande !ticket
@bot.command()
async def ticket(ctx, *message):
    '''Envoie un ticket au service d'administration du serveur: faites !ticket (votre message)'''
    global supprimerUnMessage
    channel = discord.utils.get(ctx.guild.channels, name="❔ticket-administrateur❔")
    channel_id = channel.id
    auteur = ctx.author.mention
    if channel_id == 826437578701144114:
        await ctx.message.delete() #Supprime le message de la personne ayant rentré la commande
        txt = ' '.join(message) #Permet de mettre un espace entre chaque tuple de la variable message
        salon = discord.utils.get(ctx.guild.channels, name="chat-admins") #Initialise la variable salon sur le nom d'un salon dans name
        emoji = "✔"
        global monMessage
        monMessage = await salon.send(f"{administrateur} {auteur} **a envoyé le ticket suivant:** {txt}")
        await monMessage.add_reaction(emoji)

@bot.command() #Crée la commande !clash pour clasher un utilisateur random
async def clash(ctx, nouveau_membre: discord.Member):
    '''Permet de clasher un membre du discord en le mentionnant avec !clash @LePseudo'''
    pseudo = nouveau_membre.mention
    phraseDeClash = [f"Des fois je me sens super con mais quand je vois {pseudo} ça va mieux", f"L'intelligence chez {pseudo} c'est rare comme un 31 février", f"{pseudo} t’as pas léché un téton depuis que ta mère a stoppé de te donner le sein.", f"Chuis un robot et j'ai plus de talent que {pseudo} !", f"{pseudo} était mon plan A, j'etais ton plan B, tu croyais que ça allait finir en plan Q mais tu t plan T", f"J'ai alzheimer mais au moins je suis sûr de ne jamais oublier à quel point {pseudo} est complètement débile.", f"La place de la femme c'est à la cuisine mais la place de {pseudo} c'est loin de moi !"]
    await ctx.send(phraseDeClash[randint(0, len(phraseDeClash) - 1)])

@bot.command()
async def disquettePrive(ctx, member: discord.Member):
    '''Envoie une petite disquette à votre âme soeur grâce à la commande !disquettePrive @LePseudo'''
    phraseDeDisquette = [f"Dans le royaume de mon cœur, c'est toi la princesse.", f"Moi sans toi, c'est comme un océan sans eau.", f" On s'est déjà vu quelque part, non? Tu ressembles énormément à ma prochaine petite copine.", f"Si un jour ton cœur ne bat plus, je te donnerai le mien, car sans toi, il me sert à rien.", f"Si tu veux savoir pourquoi je te suis, c'est parce que mon père m'a toujours dit de poursuivre mes rêves.", f"Tu dois être fatiguée à force de trotter dans ma tête toute la journée.", f"Si à chaque fois que je pensais à toi, il poussait une fleur, alors la Terre serait un immense jardin de roses.", f"Moi sans toi, c'est comme Roméo sans Juliette.", f"J'aimerais être une feuille morte devant  ta porte pour que tu m'écrases par ta beauté à chaque fois que  tu sors de chez toi.", f"Tu n'as pas eu mal quand tu es tombée du ciel mon ange ?", f" En temps normal je suis un très bon nageur, mais là je ne comprends pas je me noie dans tes yeux.", f"Si j'étais un juge, je nous obligerai à nous aimer à perpétuité.", f"Ton père travaille chez Nintendo si j’en crois ton corps de DS", f"Dommage que tu ne sois pas mon petit orteil par ce que je t'aurais bien démonté sur tous les coins de meuble !", f"Si tu cherches le chemin du bonheur je veux bien t'avancer de 22 cm ^^", f"Hey mademoiselle vous êtes tellement belle qu'il n'y a plus besoin de virgule !", f"Tu es plus que mon bonheur, tu es toute ma vie. Plus tu es heureux, plus je le suis ; ton bonheur fait mon bonheur. Si j'étais une larme je naîtrai de tes yeux pour caresser ta joue, et mourir sur tes lèvres. Grâce à toi, tous mes rêves d'amour, même les plus insensés, sont devenus une réalité."]
    await member.send(phraseDeDisquette[randint(0, len(phraseDeDisquette) - 1)])
    await member.send(f"Ce petit message vient de {ctx.author.mention}")

# créer la commande !bienvenue @pseudo
@bot.command()
async def bienvenue(ctx, nouveau_membre: discord.Member):
    '''Souhaitez la bienvenue à un membre du discord grâce à la commande !bienvenue @LePseudo'''

    # recupere le nom
    pseudo = nouveau_membre.mention
    # executer le message de bienvenue
    await ctx.send(f"Bienvenue à {pseudo} sur le serveur discord ! N'oublie pas de faire !regles")

@bot.command()
async def test(ctx, message):
    '''Commande inutile pour le moment'''
    print(message)

@bot.command()
async def p(ctx):
    '''Commande inutile pour le moment'''
    global piedsTeenWolf
    await ctx.send(piedsTeenWolf + 1)
    await ctx.message.delete()
    piedsTeenWolf = piedsTeenWolf + 1

# verifier l'erreur
@bienvenue.error
async def on_command_error(ctx, error):
    # detecter cette erreur
    if isinstance(error, commands.MissingRequiredArgument):
        # envoyer un message
        await ctx.send("Tu dois faire !bienvenue @pseudo")

def processString(txt):
  specialChars = '{\}"",'
  for specialChar in specialChars:
    txt = txt.replace(specialChar, '')
  print(txt) 
  txt = txt.replace(',', ' ')
  return txt

def monHoroscope(signe):
    signesZodiaque = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius",
                      "Capricorn", "Aquarius", "Pisces"]
    url = f"https://devbrewer-horoscope.p.rapidapi.com/month/short/{signe}"
    headers = {
        'x-rapidapi-key': "87a382c5edmsh51597dd88bcc11cp1ae5e8jsn63ef3ac90d64",
        'x-rapidapi-host': "devbrewer-horoscope.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    return processString(response.text)

#Créer la commande !signes
@bot.command()
async def signes(ctx):
    '''Permet d'afficher la liste des signes astrologiques pour la commande !horoscope'''
    await ctx.send("Voici la liste des signes astrologiques que vous pouvez appeler avec la commande !Horoscope: **Aries**, **Taurus**, **Gemini**, **Cancer**, **Leo**, **Virgo**, **Libra**, **Scorpio**, **Sagittarius**, **Capricorn**, **Aquarius**, **Pisces**")

@bot.command()
async def horoscope(ctx, signe):
    '''Découvrez l'horoscope du mois selon le signe (vous pouvez avoir la liste de ces derniers avec la commande !signes) grâce à la commande !horoscope *votreSigne*'''
    await ctx.send(monHoroscope(signe))

@bot.command()
#Cette fonction permet de comparer deux personnes grâce à la commande !comp *personne 1* *personne 2*
async def comp(ctx, nouveau_membre1: discord.Member, nouveau_membre2: discord.Member):
    '''Permet de tester la compatibilité entre deux membre du discord grâce à la commande **!comp @LePseudo1 @LePseudo2**'''
    pseudo1 = nouveau_membre1.mention
    pseudo2= nouveau_membre2.mention
    if pseudo1 == pseudo2:
        await ctx.send("Il faut que vous indiquiez deux personnes différentes !")
    else:
        compatibilite = randint(0, 100)
        await ctx.send(f" D'après ma boule de cristal {pseudo1} et {pseudo2} sont à {compatibilite} % compatibles !")
        if compatibilite <= 40:
            gifMechant = ["https://tenor.com/view/baby-angry-eating-mad-grumpy-gif-14328548", "https://tenor.com/view/baby-baby-boy-angry-gif-12326628", "https://tenor.com/view/brat-mad-upset-tantrum-badkid-gif-5945754", "https://media1.giphy.com/media/VI2jp6o8ojW53xmupr/giphy.gif?cid=ecf05e47akqk5rm5pfzyczewmyys6ltzfib7if3xff0j0i8z&rid=giphy.gif"]
            await ctx.send(f"{gifMechant[randint(0, len(gifMechant) - 1)]}")
        if compatibilite >= 41 and compatibilite <= 70:
            gifMoyen = ["https://tenor.com/view/idk-i-dont-know-sebastian-stan-lol-wtf-gif-5364867", "https://tenor.com/view/idk-not-me-innocent-gif-5742406", "https://tenor.com/view/confused-fresh-prince-will-smith-gif-5207985", "https://tenor.com/view/stevenyeun-idk-meh-eh-shrug-gif-5140003"]
            await ctx.send(f"{gifMoyen[randint(0, len(gifMoyen) - 1)]}")
        if compatibilite >= 71:
            gifHeureux = ["https://tenor.com/view/running-hug-embrace-i-miss-you-good-to-see-you-again-gif-15965620", "https://tenor.com/view/claire-dancing-baby-sunglasses-toddler-gif-11410651", "https://tenor.com/view/-gif-4270352", "https://tenor.com/view/hug-best-friend-one-tree-hill-peyton-sawyer-brooke-davis-gif-15326502", "https://tenor.com/view/spongebob-cartoon-friends-funny-imissyou-gif-3523153", "https://tenor.com/view/friends-hug-girl-friend-best-friend-comfort-gif-16708684"]
            await ctx.send(f"{gifHeureux[randint(0, len(gifHeureux) - 1)]}")

@bot.command()
async def help(ctx):
    '''Cette commande permet de tester le bot'''
    embed=discord.Embed(title="Liste des commandes", description="**Voici la liste des commandes de DAVY:**", color=0x8a00bd)
    embed.set_author(name="DAVY", icon_url="https://image.noelshack.com/fichiers/2021/15/4/1618484589-favpng-discord-logo-user-internet-bot.png")
    embed.add_field(name="- !regles", value="Permet d'afficher les règles du serveur", inline=False)
    embed.add_field(name="- !ticket", value="Permet d'envoyer un message à l'équipe de modération du serveur grâce à !ticket (votre message)", inline=True)
    embed.add_field(name="- !signes", value="Permet d'afficher la liste des signes disponible à utiliser avec la commande horoscope", inline=True)
    embed.add_field(name="- !horoscope", value="Permet d'afficher votre horoscope grâce à la commande !horoscope (votre signe)", inline=True)
    embed.add_field(name="- !clash", value="Permet de clasher un membre du discord grâce à la commande !clash (mention d'un autre membre)", inline=True)
    embed.add_field(name="- !disquettePrive", value="Permet d'envoyer un message privé à un autre membre grâce à la commande !disquettePrive (mention d'un autre membre)", inline=True)
    embed.add_field(name="!comp", value="Compare deux utilisateurs entre eux pour vérifier si ils sont compatible utilisez !comp (mention du permier utilisateur) (mention du deuxième utilisateur)", inline=True)
    embed.set_footer(text="#Rems")
    await ctx.send(embed=embed)


# détecter quand quelqu'un ajoute un emoji sur un message
@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji  # recupere l'emoji
    canal = payload.channel_id  # recupere le numero du canal
    message = payload.message_id  # recupere le numero du message
    membre = await bot.get_guild(payload.guild_id).fetch_member(payload.user_id) #récupère l'info de l'utilisateur
    idUtilisateur = payload.user_id

    #Fonction qui ajoute un rôle à un utilisateur
    async def ajouter_role_emoji(variableRole, nomRole, canalID, messageID, nomEmoji):
        nameRole = get(bot.get_guild(payload.guild_id).roles, name=nomRole) #nomRole doit être un string
        if canal == canalID and message == messageID and emoji.name == nomEmoji: #canalID et messageID sont des INT et pas des STR
            print(f"Grade {nameRole} ajouté à {membre.name}!")
            await membre.add_roles(nameRole)
            await membre.send(F"Tu obtiens le grade: {nomRole} !")

    #Ici, le code pour le rôle League Of Legends
    await ajouter_role_emoji("lol_role", "LeagueOfLegend", 826810614168551435, 827137112910200852, "leagueoflegendslogo")

    #Ici, le code pour le rôle artiste
    await ajouter_role_emoji("artiste_role", "🎨Artiste🎨", 826810614168551435, 826812016303276034, "artiste")
    
    #Ici le code pour le rôle Rocket League
    await ajouter_role_emoji("rocketLeague_role", "Rocket League", 826810614168551435, 827137112910200852, "rocketleaguelogo")

    #Ici, le code pour le rôle Rainbow Six Siege
    await ajouter_role_emoji("rainbowsix_role", "Rainbow Six Siege", 826810614168551435, 827137112910200852, "rainbowsixlogo")
    
    #Fonction qui suprime le message de ticket traité 
    async def validerTicket(canalID, nomEmoji):
        if canal == canalID and emoji.name == nomEmoji and idUtilisateur != 823505018887340032: #canalID et messageID sont des INT et pas des STR
            print(f"{membre.name} a réglé un problème !")
            global monMessage
            await monMessage.delete() #Supprime le message du bot
            await membre.send(F"Merci d'avoir réglé le problème {membre.name} !")
            print(idUtilisateur)
    await validerTicket(675269930437836831, "✔")

    
# détecter quand quelqu'un ajoute un emoji sur un message
@bot.event
async def on_raw_reaction_remove(payload):

    emoji = payload.emoji  # recupere l'emoji
    canal = payload.channel_id  # recupere le numero du canal
    message = payload.message_id # recupere le numero du messae
    membre = await bot.get_guild(payload.guild_id).fetch_member(payload.user_id)

    #Fonction qui supprime le rôle d'un utilisateur
    async def supprimer_role_emoji(variableRole, nomRole, canalID, messageID, nomEmoji):
        nameRole = get(bot.get_guild(payload.guild_id).roles, name=nomRole) #nomRole doit être un string
        if canal == canalID and message == messageID and emoji.name == nomEmoji: #canalID et messageID sont des INT et pas des STR
            print(f"Grade {nameRole}supprimé à {membre.name}!")
            await membre.remove_roles(nameRole)
            await membre.send(F"Tu obtiens le grade: {nomRole} !")
    #Ici, code pour artiste 
    await supprimer_role_emoji("artiste_role", "🎨Artiste🎨", 826810614168551435, 826812016303276034, "artiste")
    
    #Ici, code pour league of legends
    await supprimer_role_emoji("lol_role", "LeagueOfLegend", 826810614168551435, 827137112910200852, "leagueoflegendslogo")

    #Ici, code pour Rocket League
    await supprimer_role_emoji("rocketLeague_role", "Rocket League", 826810614168551435, 827137112910200852, "rocketleaguelogo")

    #Ici, code pour Rainbow Six Siege
    await supprimer_role_emoji("rainbowsix_role", "Rainbow Six Siege", 826810614168551435, 827137112910200852, "rainbowsixlogo")
# phrase
print("Lancement de DAVY...")



token = open("token.txt", "r").read()
# connecter au serveur
bot.run(token)