import random
import generer
import config
import Bataille



def main():
    joueurs = ["Paul", "Mike"]
    bataille = Bataille(generer.Paquet(), joueurs)
    bataille.construirePaquet(14, ["carreau", "trefle", "pique", "coeur"])
    print("apres melange:")

    bataille.melangerCarte()
    bataille.distribuerCarte()
    bataille.commencer_partie()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


