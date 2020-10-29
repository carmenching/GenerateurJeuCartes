import sup
import config

class Bataille(config.Jeu):

    def commencer_partie(self):
        partie1 = Partie(self.__joueurs)
        partie1.derouler_tour(self.__joueurs)
        while partie1.verifier_partie() is False:
            joueurs_en_cours = partie1.joueurs_en_cours
            print("continue playing: ")
            Outil.printSituation(self.__joueurs)
            input("press to continue")
            partie1.derouler_tour(joueurs_en_cours)
            partie1.verifier_main()
        print("partie terminee")

    def derouler_tour(self, joueurs):
        pot = []
        for joueur in joueurs:
            print("joueur "+ joueur.surnom + " joue:")
            joueur.jouer_carte()
            pot.append(joueur.carte_actuel)

        tmp = []
        print("current cartes in pot:")
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
            joueur_gagnant = self.derouler_tour(joueurs_bataille)
            for carte in pot:
                joueur_gagnant.ajouter_debut_main(carte)
        else:
            for joueur in joueurs:
                if max(tmp) == joueur.carte_actuel.valeur:
                    print("joueur gagnant tour: "+ joueur.surnom)
                    for carte in pot:
                        joueur.ajouter_debut_main(carte)
                    return joueur
            

    def verifier_main(self):
        for joueur in self.joueurs_en_cours:
            if len(joueur.get_main()) == 0:
                self.joueurs_perdu.append(joueur)
                self.joueurs_en_cours.remove(joueur)
    
    def verifier_partie(self):
        if len(self.joueurs_en_cours) == 1 or len(self.joueurs_en_cours) < 2:
            self.joueur_gagnant = self.joueurs_en_cours[0]
            return True
        else:
            return False