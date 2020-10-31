import random
import config


class Carte:
    '''
    Classe Carte répréntant d'une carte
    ...

    Attributs:
    ----------
    description : str
        description simple d'une carte
    valeur : int
        valeur en entier d'une carte

    '''
    def __init__(self, description, valeur):
        """ Constructeur d'objet Carte
        Parameters:
        ----------
        description : str
            description simple d'une carte
        valeur : int
            valeur en entier d'une carte
        """
        self.description = description
        self.valeur = valeur

    def afficher(self):
        """Afficher la valeur et la description de la carte"""
        return "{} de {}".format(self.valeur, self.description)

class Paquet:    
    '''
    Une classe répresentant d'un Paquet - un ensemble de carte
    ...

    Attributs:
    ----------
    _cartes : list
        une liste d'objet Carte qui constitue le paquet
    '''

    def __init__(self, nbrCartes, listeValeursCartes):
        """ Constructeur d'objet Paquet
        Parameters:
        ----------
        nbrCartes : int
            nombre de cartes à créer pour le paquet
        listeValeursCartes : int
            une liste des variantes de descriptions pour chaque nbrCartes
        """
        self.construire(nbrCartes, listeValeursCartes)

    def get_cartes(self):
        """Getter défaut d'attribut protégé 'cartes'"""
        return self._cartes

    def set_cartes(self, cartes):
        """Setter défaut d'attribut protégé 'cartes'"""
        self._cartes = cartes
    
    # construire un paquet de cartes personnalisé
    def construire(self, nbrCartes, liste_valeurs):
        """construire un paquet de cartes personnalisé - méthode appelé par défaut par constructeur
        Parameters:
        -----------
        nbrCartes : int
            nombre de cartes à créer pour le paquet
        listeValeursCartes : int
            une liste des variantes de descriptions pour chaque nbrCartes
        """
        self._cartes = []
        for s in liste_valeurs:
            for valeur in range(1, nbrCartes):
                self._cartes.append(Carte(s, valeur))

    # 
    def melanger_cartes(self):
        """mélanger le paquet de cartes"""
        tmp = self.get_cartes()
        paquet = []
        while len(tmp) != 0:
            carte = random.choice(tmp)
            paquet.append(carte)
            tmp.remove(carte)
        self._cartes = paquet

    # 
    def distribuer_cartes(self, joueurs):
        """distribuer le paquet de cartes au 'param - joueurs
        Parameters:
        -----------
        joueurs : list
            une liste d'objets Joueur
        """
        tmp = self.get_cartes()
        cartes = {}
        while len(tmp) != 0:
            for joueur in joueurs:
                carte = tmp[0]
                if joueur.get_main() is None:
                    joueur.set_main([])
                joueur.ajouter_fin_main(carte)
                tmp.remove(carte)

    # 
    def enlever_cartes(self, cartes):
        """Enlever la liste de cartes du paquet
        Parameters:
        -----------
        cartes : list
            une liste d'objets Carte
        """
        for carte in cartes:
            self._cartes.remove(carte)

    # 
    def afficher(self):
        """afficher la carte du paquet"""
        for c in self._cartes:
            print(c.afficher())

# class Pioche(Paquet):
#     def __init__(self, cartes=[]):
#         self._cartes = cartes
    
#     def ajouter_cartes(self, cartes):
#         for carte in cartes:
#             self._cartes.append(carte)
