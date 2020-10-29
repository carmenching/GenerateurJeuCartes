import random
import sup as sup


def main():
    joueurs = ["Paul", "Mike", "Violet", "Alex"]
    jeu = sup.Jeu(sup.Paquet(), joueurs)
    jeu.construirePaquet(14, ["Hearts", "Club", "Diamond", "Clover"])
    jeu.construirePioches(1)
    # jeu.afficherPaquet()
    jeu.ajouterCartesDansPioche(1, 12)
    # jeu.afficher_pioche()
    jeu.melangerCarte()
    jeu.distribuerCarte()
    # # test print carte joueur
    # for joueur in jeu.get_joueurs():
    #     print(str(joueur.surnom) + ": ")
    #     for carte in joueur.get_main():
    #         print(carte.afficher() + ', ', end=" ")
    #     print('')

    # jb = Bataille()
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# TODO :
# pioche

