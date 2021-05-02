import random
class creationTournois:
    '''
    Cette classe permettra de créer un tournois de A à Z
    '''
    def __init__(self, nom_tournois): #self = méthode standard
        print("Création d'un tournois...")
        self.nom_tournois = nom_tournois
        self.equipes= []

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
    def match_end(self):
        pass

premierTournois = creationTournois("Mon tournois")

for i in range(1, 21):
    premierTournois.add_team(f"Equipe {i}")
print("Mélange des équipes")
premierTournois.shuffle_team()
print(premierTournois.equipes)
premierTournois.create_bracket()
