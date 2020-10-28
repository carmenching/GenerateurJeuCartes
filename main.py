import random


class Carte:
    def __init__(self, suite, valeur):
        self.suite = suite
        self.valeur = valeur

    def afficher(self):
        return "{} of {}".format(self.valeur, self.suite)


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

    def enlever_cartes(self, cartes):
        for carte in cartes:
            self._cartes.remove(carte)

    def afficher(self):
        for c in self._cartes:
            print(c.afficher())


class Pioche(Paquet):
    # def __init__(self):
    #     super().__init__(cartes=[])
    #     # self.__cartes = cartes

    def ajouter_cartes(self, cartes):
        for carte in cartes:
            self._cartes.append(carte)

    def afficher(self):
        for c in self._cartes:
            print(c.afficher())


class Joueur:
    def __init__(self, surnom, main=None):
        self.surnom = surnom
        self.__main = main

    def get_main(self):
        return self.__main

    def set_main(self, carte):
        self.__main = carte

    def ajouter_main(self, carte):
        self.__main.append(carte)


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
        print(pioche)
        self.__cartes.enlever_cartes(cartes_a_disposer)

    def get_pioche(self):
        return self.__pioches

    def afficher_pioche(self):
        for nbr in self.__pioches:
            pioche = self.__pioches[nbr]
            pioche.afficher()


def main():
    joueurs = ["Paul", "Mike", "Violet", "Alex"]
    jeu = Jeu(Paquet(), joueurs)
    jeu.construirePaquet(14, ["Hearts", "Club", "Diamond", "Clover"])
    jeu.construirePioches(1)
    # jeu.afficherPaquet()
    jeu.ajouterCartesDansPioche(1, 12)
    # jeu.afficherPaquet()
    # jeu.afficher_pioche()
    # jeu.construirePaquet(1, 14, ["Hearts", "Club", "Diamond", "Clover"])
    # jeu.melangerCarte()
    # jeu.distribuerCarte()
    # # test print carte joueur
    # for joueur in jeu.get_joueurs():
    #     print(str(joueur.surnom) + ": ")
    #     for carte in joueur.get_main():
    #         print(carte.afficher() + ', ', end=" ")
    #     print('')
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# TODO :
# pioche

