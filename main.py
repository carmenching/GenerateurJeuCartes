# -*- coding: utf-8 -*-
import random
import generer as generer
import config as config


def main():
    joueurs = ["Paul", "Jean"]
    bataille = config.Bataille(generer.Paquet(), joueurs)
    bataille.construirePaquet(14, ["carreau", "trefle", "pique", "coeur"])
    print("apres melange:")
    bataille.melangerCarte()
    bataille.distribuerCarte()
    bataille.commencer_partie()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


