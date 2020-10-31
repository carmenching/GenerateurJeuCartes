import random

class Outil:
    """Classe Outil - une classe utilitaire portant les méthodes à utiliser pour tous les classes"""
    @staticmethod
    def printSituation(joueurs):
        print("current hand of all players:")
        for joueur in joueurs:
            print(joueur.surnom + ": ")
            # print(joueur.get_main(), end="")
            for carte in joueur.get_main():
                print(carte.afficher()+ ", ", end="")
            print('')

