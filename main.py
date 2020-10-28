import random


class Carte():
    def __init__(self, suite, valeur):
        self.suite = suite
        self.valeur = valeur

    def afficher(self):
        return "{} of {}".format(self.valeur, self.suite)


class Paquet():
    def __init__(self):
        self.__cartes = []

    def get_cartes(self):
        return self.__cartes

    def construire(self, minimum, maximum, liste_valeurs):
        for s in liste_valeurs:
            for valeur in range(minimum, maximum):
                self.__cartes.append(Carte(s, valeur))

    def melanger_cartes(self):
        tmp = self.get_cartes()
        paquet = []
        while len(tmp) != 0:
            carte = random.choice(tmp)
            paquet.append(carte)
            tmp.remove(carte)
        self.__cartes = paquet

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

    def afficher(self):
        for c in self.__cartes:
            print("{} of {}".format(c.valeur, c.suite))

class Pioche(Paquet):
    def __init__(self):
        super().__init__()

class Joueur():
    def __init__(self, surnom, main=None):
        self.surnom = surnom
        self.__main = main

    def get_main(self):
        return self.__main

    def set_main(self, carte):
        self.__main = carte

    def ajouter_main(self, carte):
        self.__main.append(carte)


class Jeu():
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

    def construirePaquet(self, minimum, maximum, joueurs):
        self.__cartes.construire(minimum, maximum, joueurs)


def main():
    joueurs = ["Paul", "Mike", "Violet", "Alex"]
    jeu = Jeu(Paquet(), joueurs)
    jeu.construirePaquet(1, 14, ["Hearts", "Club", "Diamond", "Clover"])
    jeu.melangerCarte()
    jeu.distribuerCarte()
    # test print carte joueur
    for joueur in jeu.get_joueurs():
        print(str(joueur.surnom) + ": ")
        for carte in joueur.get_main():
            print(carte.afficher() + ', ', end=" ")
        print('')
    pioche = Pioche()
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

