import random

class Carte:
    def __init__(self, suite, valeur):
        self.suite = suite
        self.valeur = valeur

    def afficher(self):
        return "{} de {}".format(self.valeur, self.suite)


class Paquet:
    def __init__(self, cartes=[]):
        self.set_cartes(cartes)

    def get_cartes(self):
        return self._cartes

    def set_cartes(self, cartes):
        self._cartes = cartes

    def construire(self, nombre, liste_valeurs):
        for s in liste_valeurs:
            for valeur in range(1, nombre):
                self._cartes.append(Carte(s, valeur))

    def melanger_cartes(self):
        tmp = self.get_cartes()
        paquet = []
        while len(tmp) != 0:
            carte = random.choice(tmp)
            paquet.append(carte)
            tmp.remove(carte)
        self._cartes = paquet

    def distribuer_cartes(self, joueurs):
        tmp = self.get_cartes()
        cartes = {}
        while len(tmp) != 0:
            for joueur in joueurs:
                carte = tmp[0]
                if joueur.get_main() is None:
                    joueur.set_main([])
                    joueur.ajouter_main(carte)
                else:
                    joueur.ajouter_main(carte)
                tmp.remove(carte)

    def enlever_cartes(self, cartes):
        for carte in cartes:
            self._cartes.remove(carte)

    def afficher(self):
        for c in self._cartes:
            print(c.afficher())


class Pioche(Paquet):
    def __init__(self, cartes=[]):
        self._cartes = cartes
    
    def ajouter_cartes(self, cartes):
        for carte in cartes:
            self._cartes.append(carte)


class Joueur:
    def __init__(self, surnom, main=None, carte=None):
        self.surnom = surnom
        self.__main = main
        self.carte_actuel = carte

    def get_main(self):
        return self.__main

    def set_main(self, carte):
        self.__main = carte

    def ajouter_main(self, carte):
        self.__main.append(carte)

    def jouer_carte(self):
        carte_joue = self.__main[-1]
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
        # print("cartes à disposer: " + str(cartes_a_disposer))
        self.__pioches[piocheNbr - 1].ajouter_cartes(cartes_a_disposer)
        pioche = self.__pioches[piocheNbr - 1]
        self.__cartes.enlever_cartes(cartes_a_disposer)

    def get_pioche(self):
        return self.__pioches

    def afficher_pioche(self):
        for nbr in self.__pioches:
            pioche = self.__pioches[nbr]
            pioche.afficher()

    def commencer_partie(self):
        partie1 = Partie(self.__joueurs)
        partie1.derouler_tour()
        while partie1.verifier_partie() is False:
            print("continue playing: ")
            printSituation(self.__joueurs)
            input("press to continue")
            partie1.derouler_tour()

        print("partie terminee")


class Partie:
    def __init__(self, joueurs, joueur_gagnant=None):
        self.joueurs_en_cours = joueurs
        self.joueurs_perdu = []
        self.joueur_gagnant = joueur_gagnant

    def derouler_tour(self):
        pot = []
        for joueur in self.joueurs_en_cours:
            joueur.jouer_carte()
            pot.append(joueur.carte_actuel)
        for joueur in self.joueurs_en_cours:
            tmp = []
            for carte in pot:
                tmp.append(carte.valeur)
            if max(tmp) == joueur.carte_actuel.valeur:
                for carte in pot:
                    joueur.ajouter_main(carte)
            self.verifier_main(joueur)   
            
    def verifier_main(self, joueur):
        if len(joueur.get_main()) == 0:
            self.joueurs_perdu.append(joueur)
            self.joueurs_en_cours.remove(joueur)
    
    def verifier_partie(self):
        if len(self.joueurs_en_cours) == 1 or len(self.joueurs_en_cours) < 2:
            self.joueur_gagnant = self.joueurs_en_cours[0]
            return True
        else:
            return False

# class Tour:
#     def __init__(self, joueur):
#         self.joueur = joueura



# class Bataille(Jeu):

def printSituation(joueurs):
    print("current hand of all players:")
    for joueur in joueurs:
        print(joueur.surnom + ": ")
        # print(joueur.get_main(), end="")
        for carte in joueur.get_main():
            print(carte.afficher()+ ", ", end="")
        print('')

    
#     pass

def main():
    joueurs = ["Paul", "Mike", "Violet", "Alex"]
    jeu = Jeu(Paquet(), joueurs)
    jeu.construirePaquet(14, ["carreau", "trefle", "pique", "coeur"])
    # jeu.construirePioches(1)
    # jeu.afficherPaquet()
    # jeu.ajouterCartesDansPioche(1, 12)
    # jeu.afficher_pioche()
    print("apres melange:")
    jeu.afficherPaquet()

    jeu.melangerCarte()
    jeu.distribuerCarte()
    jeu.commencer_partie()


    # test print carte joueur
    

    # jb = Bataille()
    pass

if __name__ == '__main__':
    main()