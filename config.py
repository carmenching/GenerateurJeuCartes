import random
from sup import Outil

class Joueur:
    def __init__(self, surnom, main=None, carte=None):
        self.surnom = surnom
        self.__main = main
        self.carte_actuel = carte

    def get_main(self):
        return self.__main

    def set_main(self, carte):
        self.__main = carte

    def ajouter_fin_main(self, carte):
        self.__main.append(carte)

    def ajouter_debut_main(self, carte):
        self.__main.insert(0, carte)

    def jouer_carte(self):
        carte_joue = self.__main[-1]
        print(carte_joue.afficher())
        self.__main.remove(carte_joue)
        self.carte_actuel = carte_joue

class Jeu:
    def __init__(self, cartes, joueurs):
        self.__cartes = cartes
        self.set_joueurs(joueurs)

    def get_joueurs(self):
        return self.__joueurs

    def set_joueurs(self, joueurs):
        liste_joueurs = []
        for joueur in joueurs:
            liste_joueurs.append(Joueur(joueur))
        self.__joueurs = liste_joueurs

    def afficherJoueurs(self):
        print("Joueurs: ")
        for joueur in self.__joueurs:
            print(joueur.surnom)

    def afficherPaquet(self):
        print("Paquet de cartes:")
        self.__cartes.afficher()

    def melangerCarte(self):
        self.__cartes.melanger_cartes()

    def distribuerCarte(self):
        self.__cartes.distribuer_cartes(self.__joueurs)

    def construirePaquet(self, nombre, joueurs):
        self.__cartes.construire(nombre, joueurs)

    def construirePioches(self, pioches):
        if pioches is not None:
            self.__pioches = {}
            for nbr in range(pioches):
                self.__pioches[nbr] = Pioche()

    def ajouterCartesDansPioche(self, piocheNbr, nbrCartes):
        cartes_a_disposer = random.sample(self.__cartes.get_cartes(), nbrCartes)
        self.__pioches[piocheNbr - 1].ajouter_cartes(cartes_a_disposer)
        pioche = self.__pioches[piocheNbr - 1]
        self.__cartes.enlever_cartes(cartes_a_disposer)

    def get_pioche(self):
        return self.__pioches

    def afficher_pioche(self):
        for nbr in self.__pioches:
            pioche = self.__pioches[nbr]
            pioche.afficher()

    

class Partie:
    def __init__(self, joueurs, joueur_gagnant=None):
        self.joueurs_en_cours = joueurs
        self.joueurs_perdu = []
        self.joueur_gagnant = joueur_gagnant

    # def derouler_tour(self, joueurs):
    #     pot = []
    #     for joueur in joueurs:
    #         print("joueur "+ joueur.surnom + " joue:")
    #         joueur.jouer_carte()
    #         pot.append(joueur.carte_actuel)

    #     tmp = []
    #     print("current cartes in pot:")
    #     for carte in pot:
    #         print(carte.afficher()+ ", ", end="")
    #         tmp.append(carte.valeur)
        
    #     if len(set(tmp)) != len(tmp):
    #         print("yay")
    #         tmp_set = set(tmp)
    #         tmp = list(tmp_set)
    #         joueurs_bataille = []
    #         for joueur in joueurs:
    #             if max(tmp) == joueur.carte_actuel.valeur:
    #                 joueurs_bataille.append(joueur)
    #         joueur_gagnant = self.derouler_tour(joueurs_bataille)
    #         for carte in pot:
    #             joueur_gagnant.ajouter_debut_main(carte)
    #     else:
    #         for joueur in joueurs:
    #             if max(tmp) == joueur.carte_actuel.valeur:
    #                 print("joueur gagnant tour: "+ joueur.surnom)
    #                 for carte in pot:
    #                     joueur.ajouter_debut_main(carte)
    #                 return joueur
            

    # def verifier_main(self):
    #     for joueur in self.joueurs_en_cours:
    #         if len(joueur.get_main()) == 0:
    #             self.joueurs_perdu.append(joueur)
    #             self.joueurs_en_cours.remove(joueur)
    
    # def verifier_partie(self):
    #     if len(self.joueurs_en_cours) == 1 or len(self.joueurs_en_cours) < 2:
    #         self.joueur_gagnant = self.joueurs_en_cours[0]
    #         return True
    #     else:
    #         return False

    
