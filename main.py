# -*- coding: utf-8 -*-
import random
import generer as generer
import config as config


def main():
    # fournir une liste de joueurs (liste de chaînes)
    joueurs = ["Paul", "Jean"]
    # tester avec un jeu de bataille
    bataille = config.Bataille(14, ["carreau", "trefle", "pique", "coeur"], joueurs)
    # mélanger les cartes, distribuer les cartes et commencer la partie de bataille fermée
    bataille.melangerCarte()
    bataille.distribuerCarte()
    bataille.commencer_partie()


if __name__ == '__main__':
    main()


