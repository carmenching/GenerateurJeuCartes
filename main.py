# -*- coding: utf-8 -*-
import random
import objetJeu as objetJeu
import config as config


def main():
    """Tester le jeu de bataille fermée"""
    # fournir une liste de joueurs (liste de chaînes)
    joueurs = ["Paul", "Jean"]
    # tester avec un jeu de bataille
    bataille = config.Bataille(13, ["carreau", "trefle", "pique", "coeur"], joueurs)
    # mélanger les cartes, distribuer les cartes et commencer la partie de bataille fermée
    bataille.melangerCarte()
    bataille.distribuerCarte(len(bataille._paquet._cartes))
    bataille.commencer_partie()

if __name__ == '__main__':
    main()


