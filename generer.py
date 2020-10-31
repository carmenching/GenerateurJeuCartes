import random
import config


class Carte:
    '''
    Classe Carte répréntant d'une carte
    ...

    Attributs:
    ----------
    suite : str
        description simple d'une carte

    '''
    def __init__(self, description, valeur):
        self.description = description
        self.valeur = valeur

    def afficher(self):
        return "{} de {}".format(self.valeur, self.description)

class Paquet:    
    '''
    une classe répresentant d'un Paquet - un ensemble de carte
    ...

    Attributs:

    '''
    # def __init__(self, cartes=[]):
    #     self.set_cartes(cartes)
    def __init__(self, nbrCartes, listeValeursCartes):
        self.construire(nbrCartes, listeValeursCartes)

    def get_cartes(self):
        return self._cartes

    def set_cartes(self, cartes):
        self._cartes = cartes
    
    # construire un paquet de cartes personnalisé
    def construire(self, nombre, liste_valeurs):
        self._cartes = []
        for s in liste_valeurs:
            for valeur in range(1, nombre):
                self._cartes.append(Carte(s, valeur))

    # construire un paquet de cartes personnalisé
    # def construire(self, nombre, liste_valeurs):
    #     for s in liste_valeurs:
    #         for valeur in range(1, nombre):
    #             self._cartes.append(Carte(s, valeur))

    # mélanger le paquet de cartes
    def melanger_cartes(self):
        tmp = self.get_cartes()
        paquet = []
        while len(tmp) != 0:
            carte = random.choice(tmp)
            paquet.append(carte)
            tmp.remove(carte)
        self._cartes = paquet

    # distribuer le paquet de cartes au 'param - joueurs
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

    # enlever la liste de cartes du paquet
    def enlever_cartes(self, cartes):
        for carte in cartes:
            self._cartes.remove(carte)

    # afficher la carte du paquet
    def afficher(self):
        for c in self._cartes:
            print(c.afficher())

# class Pioche(Paquet):
#     def __init__(self, cartes=[]):
#         self._cartes = cartes
    
#     def ajouter_cartes(self, cartes):
#         for carte in cartes:
#             self._cartes.append(carte)
