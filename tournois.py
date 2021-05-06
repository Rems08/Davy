from random import*
import random
#Idée: créer un embed nommé "info tournois" ça permettre d'enregistrer premier tour, deuxième tour etc. 
#embed=discord.Embed(title="{nom_tournois}", description="Voici les résumé du {nombre de tour} tour", color=0xffff00)
#embed.set_author(name="DAVY")
#embed.add_field(name="{Team number} vs {Team number}", value="Team number gagne 1 à 0", inline=True)
#embed.add_field(name="{Team number} vs {Team number}", value="Team nubmer gagne 7 à 3", inline=True)
#embed.set_footer(text="#Test")
#await ctx.send(embed=embed)
class creationTournois:
    '''
    Cette classe permettra de créer un tournois de A à Z
    '''
    def __init__(self, nom_tournois): #self = méthode standard
        print("Création d'un tournois...")
        self.nom_tournois = nom_tournois
        self.equipes= []
        self.equipes_score = {

        }
        self.equipes_temp = []

    def add_team(self, nom_equipe): 
        self.equipes.append(nom_equipe)

    def delete_team(self, nom_equipe):
        if nom_equipe in self.equipes:
            self.equipes.pop(self.equipes.index(nom_equipe))
        else:
            print(f"Une erreur est survenue vérifier que {nom_equipe} est bien enregistré dans le tournois")

    def shuffle_team(self):
        random.shuffle(self.equipes)

    def create_bracket(self):
        self.equipes = list(zip(*[iter(self.equipes)]*2))
        for i, j in self.equipes:
            print(f"{i} est contre {j}")

    def add_score(self, nomEquipe = str, score = int):
        presence = False
        for i, j in self.equipes:
            if j == nomEquipe or i ==nomEquipe:
                self.equipes_score[nomEquipe] = score
                presence = True
        if presence == False:
            print(f'{nomEquipe} ne fait pas partie de la liste des équipes inscrites')
    
    def show_score(self, arg):
        if arg == "all":
            print(self.equipes_score)

        if arg in self.equipes_score:
            print(f"{arg} a optenu un score de: {self.equipes_score[arg]}")

    def next_match(self):
        print("Resultat du match (Avec l'embed discord pour résumer les match précédents)")
        for i, j in self.equipes:
            if self.equipes_score[j] > self.equipes_score[i]:
                self.equipes_temp.append(j)
            if self.equipes_score[i] > self.equipes_score[j]:
                self.equipes_temp.append(i)
            if self.equipes_score[i] == self.equipes_score[j]:
                print("Il y a égalité recommencez le match !")
            
        self.equipes[:] = []
        print("La liste à ce moment là c'est", self.equipes)
        for i in self.equipes_temp:
                self.equipes.append(i)
        print(self.equipes)
        if len(self.equipes) < 3:
            for i in self.equipes:
                print(f"Félicitation au vainqueur :{i} avec un score de {self.equipes_score[i]}")
        self.equipes_temp[:] = []

premierTournois = creationTournois("Mon tournois")
premierTournois.add_team("Team 1")
premierTournois.add_team("Team 2")
premierTournois.add_team("Team 3")
premierTournois.add_team("Team 4")
premierTournois.add_team("Team 5")
premierTournois.add_team("Team 6")
premierTournois.shuffle_team()
premierTournois.create_bracket()
premierTournois.add_score("Team 1", 2)
premierTournois.add_score("Team 2", 7)
premierTournois.add_score("Team 3", 4)
premierTournois.add_score("Team 4", 6)
premierTournois.add_score("Team 5", 2)
premierTournois.add_score("Team 6", 9)
premierTournois.show_score("all")
premierTournois.next_match()
premierTournois.create_bracket()
premierTournois.next_match()
premierTournois.create_bracket()
premierTournois.next_match()