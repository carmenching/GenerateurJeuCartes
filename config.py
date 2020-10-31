import random
import objetJeu

class Joueur:
    """
    Classe Joueur réprésentant d'un joueur
    ...

    Attributes:
    ---------
    surnom : str
        le nom du joueur 

    __main : list
        Un ensemble de cartes constitue le main du joueur 

    carte_actuel : Carte
        la carte joué en actuel par le joueur
    """
    def __init__(self, surnom, main=None, carte=None):
        """ Constructeur d'objet Joueur
        Parameters:
        ----------
        surnom : str
            le nom du joueur 
        main : None
            Un objet vide qui sera remplacé par une liste d'objets Carte
        carte : None
            Un objet vide qui sera remplacé par un objet Carte pour chaque tour de chaque partie 
        """
        self.surnom = surnom
        self.__main = main
        self.carte_actuel = carte

    def get_main(self):
        """getter defaut d'attribut privé 'main'"""
        return self.__main

    def set_main(self, carte):
        """setter defaut d'attribut privé 'main'"""
        self.__main = carte

    def ajouter_fin_main(self, carte):
        """ajouter une carte à la fin du main de joueur
        Parameters:
        -----------
        carte : Carte
            l'objet carte à ajouter au main du joueur
        """
        self.__main.append(carte)

    def ajouter_debut_main(self, carte):
        """ajouter une carte au début du main de joueur
        Parameters:
        -----------
        carte : Carte
            l'objet carte à ajouter au main du joueur
        """

        self.__main.insert(0, carte)
    
    def ajouter_liste_cartes_debut_main(self, cartes):
        """ajouter une liste de cartes au début du main de joueur 
        Parameters:
        -----------
        cartes : list
            liste d'objet carte à ajouter au main du joueur
        """
        for carte in cartes:
            self.__main.insert(0, carte)

    def jouer_carte(self):
        """ajouter une liste de cartes au début du main de joueur """
        carte_joue = self.__main[-1]
        print(carte_joue.afficher())
        self.__main.remove(carte_joue)
        self.carte_actuel = carte_joue

    def jeter_carte(self):
        """abandoner une carte du main """
        carte_jeter = self.__main[-1]
        self.__main.remove(carte_jeter)
        return carte_jeter


class Jeu:
    """
    Classe Jeu à être hérité pour créer le jeu

    ...

    Attributes:
    ---------
    _joueurs : list
        une liste d'objets Joueur crées en fonction des chaînes fournit 

    _cartes : Paquet
        le paquet de carte générer pour le jeu
    """
    def __init__(self, nbrCartes, listeValeursCartes, joueurs):
        self.construirePaquet(nbrCartes, listeValeursCartes)
        self.configurerJoueurs(joueurs)
        """ Constructeur d'objet Jeu
        Parameters:
        ----------
        nbrCartes : int
            Le nombre de cartes à créer pour le paquet de cartes initial
        listeValeursCartes : str
            Une liste de valeurs pour la création du paquet de cartes initial
        joueurs : list
            Une liste de chaînes pour la création des objets Joueur 
        """

    def get_joueurs(self):
        """getter défaut d'attribut protégé joueurs"""
        return self._joueurs

    def configurerJoueurs(self, joueurs):
        """Configurer les joueurs
        Parameters:
        ----------
        joueurs : list
            Une liste de chaînes pour la création des objets Joueur 
        """
        liste_joueurs = []
        for joueur in joueurs:
            liste_joueurs.append(Joueur(joueur))
        self._joueurs = liste_joueurs

    def afficherJoueurs(self):
        """ Afficher des joueurs d'objet Jeu"""
        print("Joueurs: ")
        for joueur in self._joueurs:
            print(joueur.surnom)

    def _afficherPaquet(self):
        """Afficher le paquet"""
        print("Paquet de cartes:")
        self._paquet.afficher()

    def melangerCarte(self):
        """Mélanger les cartes dans le paquet"""
        self._paquet.melanger_cartes()

    def distribuerCarte(self, nbrCartes):
        """Distribuer les cartes dans le paquet aux joueurs"""
        self._paquet.distribuer_cartes(self._joueurs, nbrCartes)

    def construirePaquet(self, nbrCartes, listeValeursCartes):
        """Distribuer les cartes dans le paquet aux joueurs
        
        Parameters:
        -----------
        nbrCartes : int
            Le nombre de cartes à créer pour le paquet de cartes initial
        listeValeursCartes : str
            Une liste de valeurs pour la création du paquet de cartes initial
        """
        self._paquet = objetJeu.Paquet()
        self._paquet.construire(nbrCartes, listeValeursCartes)

    def construirePioches(self, nbrPioches):
        """Construire des pioches pour le jeu
        
        Parameters:
        -----------
        pioches : int
            Le nombre de pioche à créer pour jeu
        """
        self._pioches = {}
        for nbr in range(nbrPioches):
            self._pioches[nbr] = objetJeu.Pioche()

    def ajouterCartesDansPioche(self, piocheNbr, cartes):
        """Ajouter les cartes dans la pioche sélectionné
        
        Parameters:
        -----------
        piocheNbr : int
            L'id en entier de pioche
        cartes : list
            le nombre de carte
        """
        self._pioches[piocheNbr - 1].ajouter_cartes(cartes)
        self._paquet.enlever_cartes(cartes)

    def get_pioche(self):
        """Getter défaut des pioches"""
        return self._pioches

    def ajouterCartesAuPlateuJeu(self):
        """Ajouter la reste de cartes non distribué dans le plateau de jeu"""
        if len(self._paquet._cartes) != 0:
            print("cartes restant")
            self._plateauJeu = objetJeu.PlateauJeu()
            self._plateauJeu.ajouter_cartes(self._paquet._cartes)
         

class Partie:
    """Classe partie qui stocke les informations des joueurs

    ...

    Attributes:
    ---------
    joueurs_en_cours : list
        une liste de joueurs en cours de joueur la partie 

    joueurs_perdu : list
        une liste de joueurs qui ont perdus la partie
    
    joueur_gagnant : Joueur
        le joueur qui a gagné la partie

    """
    def __init__(self, joueurs, joueur_gagnant=None):
        """ Constructeur d'objet Partie
        Parameters:
        ----------
        joueurs : list
            une liste d'objets Joueur 
        joueur_gagnant : None
            Un objet vide qui sera remplacé par un objet Joueur
        """
        self.joueurs_en_cours = joueurs
        self.joueurs_perdu = []
        self.joueur_gagnant = joueur_gagnant



class Bataille(Jeu):
    """Teste création d'un jeu de bataille en héritant la classe Jeu, attributs : idem classe Jeu"""
    def commencer_partie(self):
        """lancer la partie"""
        self.__partie = Partie(self._joueurs)
        self.derouler_manche(self.__partie.joueurs_en_cours)
        while self.verifier_partie() is False:
            joueurs_en_cours = self.__partie.joueurs_en_cours
            print("prochaine manche: --------------------------------------")
            # input("press to continue")
            self.derouler_manche(joueurs_en_cours)
            self.verifier_main()
        print("partie terminee:")
        print(self.__partie.joueur_gagnant.surnom + " a gagné!")

    
    def derouler_manche(self, joueurs):
        """
        Action à réaliser pour chaque manche - régles de jeu de bataille
        ---> Je n'arrive pas à récupérer la valeur retourné par la méthode récursive marqué **

        Attributes:
        ---------
        joueurs : list
        une liste de joueurs en cours de joueur la partie 
        """
        pot = []
        for joueur in joueurs:
            print("joueur "+ joueur.surnom + " joue:")
            if len(joueur.get_main()) != 0 : 
                joueur.jouer_carte()
                pot.append(joueur.carte_actuel)
            else:
                self.__partie.joueurs_perdu.append(joueur)
                self.__partie.joueurs_en_cours.remove(joueur)
                return

        tmp = []
        print("cartes actuelles dans le pot:")
        for carte in pot:
            print(carte.afficher()+ ", ", end="")
            tmp.append(carte.valeur)
        print("")
        
        if len(set(tmp)) != len(tmp):
            tmp_set = set(tmp)
            tmp = list(tmp_set)
            joueurs_bataille = []
            for joueur in joueurs:
                if max(tmp) == joueur.carte_actuel.valeur:
                    joueurs_bataille.append(joueur)
            if len(joueurs_bataille) > 1:
                for joueur in joueurs_bataille:
                    if len(joueur.get_main()) != 0:
                        pot.append(joueur.jeter_carte())
                    else:
                        return
                self.commencer_bataille(joueurs_bataille, pot)

        else:
            for joueur in joueurs:
                if max(tmp) == joueur.carte_actuel.valeur:
                    print("joueur gagnant manche: "+ joueur.surnom)
                    for carte in pot:
                        joueur.ajouter_debut_main(carte)
                    return
                                
    def commencer_bataille(self, joueurs, potPrecedent):
        pot = []
        print("cartes actuelles dans le pot avant la bataille:")
        for carte in potPrecedent:
            print(carte.afficher()+ ", ", end="")
        print("")
        print("----------------------------------------------")
        print("Bataille!")
        # chaque joueur joue une carte
        for joueur in joueurs:
            print("joueur "+ joueur.surnom + " joue:")
            if len(joueur.get_main()) != 0 : 
                joueur.jouer_carte()
                pot.append(joueur.carte_actuel)
            else:
                self.__partie.joueurs_perdu.append(joueur)
                self.__partie.joueurs_en_cours.remove(joueur)
                return

        # évaluer la carte dans le pot
        tmp = []
        print("cartes actuelles dans le pot:")
        for carte in pot:
            print(carte.afficher()+ ", ", end="")
            tmp.append(carte.valeur)
        print("")
        print("----------------------------------------------")


        # vérifier s'il existe des cartes avec les mêmes valeur
        if len(set(tmp)) != len(tmp):
            tmp_set = set(tmp)
            tmp = list(tmp_set)
            joueurs_bataille = []
            for joueur in joueurs:
                if max(tmp) == joueur.carte_actuel.valeur:
                    joueurs_bataille.append(joueur)
            # si deux ou plus de joueurs ou plus ont joué une carte de même valeur
            if len(joueurs_bataille) > 1:
                for joueur in joueurs_bataille:
                    if len(joueur.get_main()) != 0:
                        pot.append(joueur.jeter_carte())
                    else:
                        return
                self.commencer_bataille(joueurs_bataille, pot)

        else:
            for joueur in joueurs:
                if max(tmp) == joueur.carte_actuel.valeur:
                    print("joueur gagnant la bataille: "+ joueur.surnom)
                    for carte in pot:
                        joueur.ajouter_debut_main(carte)
                    joueur.ajouter_liste_cartes_debut_main(potPrecedent)
                    return

        print("----------------------------------------------")
                      
    def verifier_main(self):
        """à la fin de chaque manche, les mains de chaque joueur sont vérifiés"""
        for joueur in self.__partie.joueurs_en_cours:
            if len(joueur.get_main()) == 0:
                self.__partie.joueurs_perdu.append(joueur)
                self.__partie.joueurs_en_cours.remove(joueur)
    
    def verifier_partie(self):
        """vérifier si la partie est terminé s'il ne reste qu'un joueur qui possède des cartes"""
        if len(self.__partie.joueurs_en_cours) == 1 or len(self.__partie.joueurs_en_cours) < 2:
            self.__partie.joueur_gagnant = self.__partie.joueurs_en_cours[0]
            return True
        else:
            return False

    