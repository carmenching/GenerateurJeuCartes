
class Carte():
    def __init__(self, suite, valeur):
        self.suite = suite
        self.valeur = valeur

    def afficher(self):
        print("{} of {}".format(self.valeur, self.suite))


class Paquet():
    def __init__(self, min, max, liste_valeurs):
        self.__cards = []
        self.construire(min, max, liste_valeurs)

    def construire(self, min, max, liste_valeurs):
        for s in liste_valeurs:
            for valeur in range(min, max):
                self.__cards.append(Carte(s, valeur))

    def afficher(self):
        for c in self.__cards:
            print("{} of {}".format(c.valeur, c.suite))


class Joueur():
    def __init__(self, surnom, main=None):
        self.surnom = surnom
        self.__main = main

    @property
    def get_main(self):
        return self.__main

    @get_main.setter
    def set_main(self, valeur):
        self.__main = valeur


class Jeu():
    def __init__(self, cartes, joueurs):
        self.cartes = cartes
        self.__set_joueurs(joueurs)

    def __set_joueurs(self, joueurs):
        liste_joueurs = []
        for joueur in joueurs:
            liste_joueurs.append(joueur)
        self.__joueurs = liste_joueurs

    def afficher(self):
        print("Joueurs: ")
        for joueur in self.__joueurs:
            print(joueur.surnom)
        print("Paquet de cartes:")




    # def distribuerCartes(self):


def main():
    joueurs = ["Paul", "Mike", "Violet", "Alex"]
    jeu = Jeu(Paquet(1,14, ["Hearts", "Club", "Diamond", "Clover"]), joueurs)
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
