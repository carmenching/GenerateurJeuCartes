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
    
    def ajouter_liste_cartes_debut_main(self, cartes):
        for carte in cartes:
            self.__main.insert(0, carte)

    def jouer_carte(self):
        carte_joue = self.__main[-1]
        print(carte_joue.afficher())
        self.__main.remove(carte_joue)
        self.carte_actuel = carte_joue

    def jeter_carte(self):
        carte_jeter = self.__main[-1]
        self.__main.remove(carte_jeter)
        return carte_jeter

'''
Classe Jeu à être hérité pour créer le jeu
'''
class Jeu:
    def __init__(self, cartes, joueurs):
        self._cartes = cartes
        self.set_joueurs(joueurs)

    def get_joueurs(self):
        return self._joueurs

    def set_joueurs(self, joueurs):
        liste_joueurs = []
        for joueur in joueurs:
            liste_joueurs.append(Joueur(joueur))
        self._joueurs = liste_joueurs

    # afficher les noms de joueurs
    def afficherJoueurs(self):
        print("Joueurs: ")
        for joueur in self._joueurs:
            print(joueur.surnom)

    def afficherPaquet(self):
        print("Paquet de cartes:")
        self._cartes.afficher()

    def melangerCarte(self):
        self._cartes.melanger_cartes()

    def distribuerCarte(self):
        self._cartes.distribuer_cartes(self._joueurs)

    def construirePaquet(self, nombre, joueurs):
        self._cartes.construire(nombre, joueurs)

    def construirePioches(self, pioches):
        if pioches is not None:
            self._pioches = {}
            for nbr in range(pioches):
                self._pioches[nbr] = Pioche()

    def ajouterCartesDansPioche(self, piocheNbr, nbrCartes):
        cartes_a_disposer = random.sample(self._cartes.get_cartes(), nbrCartes)
        self._pioches[piocheNbr - 1].ajouter_cartes(cartes_a_disposer)
        pioche = self._pioches[piocheNbr - 1]
        self._cartes.enlever_cartes(cartes_a_disposer)

    def get_pioche(self):
        return self._pioches

    def afficher_pioche(self):
        for nbr in self._pioches:
            pioche = self._pioches[nbr]
            pioche.afficher()    

'''
Classe partie qui stocke les informations des joueurs
'''
class Partie:
    def __init__(self, joueurs, joueur_gagnant=None):
        self.joueurs_en_cours = joueurs
        self.joueurs_perdu = []
        self.joueur_gagnant = joueur_gagnant


'''
Teste création d'un jeu de bataille en héritant la classe Jeu
'''
class Bataille(Jeu):
    # lancer la partie
    def commencer_partie(self):
        self.__partie = Partie(self._joueurs)
        self.derouler_manche(self.__partie.joueurs_en_cours)
        while self.verifier_partie() is False:
            joueurs_en_cours = self.__partie.joueurs_en_cours
            print("prochaine manche: --------------------------------------")
            Outil.printSituation(self._joueurs)
            # input("press to continue")
            self.derouler_manche(joueurs_en_cours)
            self.verifier_main()
        print("partie terminee:")
        print(self.__partie.joueur_gagnant.surnom + " a gagné!")

    '''
    Action à réaliser pour chaque manche - régles de jeu de bataille
    - Je n'arrive pas à récupérer la valeur retourné par la méthode récursive marqué **
    '''
    def derouler_manche(self, joueurs):
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
        
        if len(set(tmp)) != len(tmp):
            print("yay")
            tmp_set = set(tmp)
            tmp = list(tmp_set)
            joueurs_bataille = []
            for joueur in joueurs:
                if max(tmp) == joueur.carte_actuel.valeur:
                    joueurs_bataille.append(joueur)
                    for joueur in joueurs_bataille:
                        pot.append(joueur.jeter_carte())
            #**
            joueur_gagnant = self.derouler_manche(joueurs_bataille)
            for carte in pot:
                joueur_gagnant.ajouter_debut_main(carte)
        else:
            
            for joueur in joueurs:
                print("loop " + joueur.surnom)
                if max(tmp) == joueur.carte_actuel.valeur:
                    print("joueur gagnant manche: "+ joueur.surnom)
                    for carte in pot:
                        joueur.ajouter_debut_main(carte)
                    print("avant return: joueur = " + joueur.surnom)
                    return joueur
                
    # à la fin de chaque manche, les mains de chaque joueur sont vérifiés                
    def verifier_main(self):
        for joueur in self.__partie.joueurs_en_cours:
            if len(joueur.get_main()) == 0:
                self.__partie.joueurs_perdu.append(joueur)
                self.__partie.joueurs_en_cours.remove(joueur)
    
    # vérifier si la partie est terminé s'il ne reste qu'un joueur qui possède des cartes
    def verifier_partie(self):
        print(self.__partie.joueurs_en_cours)
        if len(self.__partie.joueurs_en_cours) == 1 or len(self.__partie.joueurs_en_cours) < 2:
            self.__partie.joueur_gagnant = self.__partie.joueurs_en_cours[0]
            return True
        else:
            return False