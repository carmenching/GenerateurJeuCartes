import random
import config

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
                joueur.ajouter_fin_main(carte)
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
