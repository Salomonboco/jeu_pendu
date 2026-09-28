import random
import string
from mots import mots

# Initialisation du score global à zéro
score = 0
nom_joueur = ""

# Fonction qui choisit un mot au hasard dans la liste fournie
def choisir_mot(mots):
    mot = random.choice(mots)  # Sélectionne aléatoirement un mot
    return mot

# Fonction qui demande au joueur s'il souhaite rejouer ou quitter la partie
def jouer_de_nouveau():
    # Demande initiale de saisie au joueur
    jouer_jeu = input("Souhaitez-vous continuer à jouer? (O = Oui, N = Non)")

    # Boucle de contrôle : continue de demander tant que la réponse n'est pas valide (O, o, N ou n)
    while jouer_jeu not in {"O", "o", "N","n"}:
        jouer_jeu = input("Souhaitez-vous continuer à jouer? (O = Oui, N = Non)")

    # Si le joueur répond Oui ("O" ou "o"), on relance une nouvelle partie
    if jouer_jeu == "O" or jouer_jeu == "o":
        hangman()

    # Si le joueur répond Non ("N" ou "n"), on affiche un message et on ferme le programme
    elif jouer_jeu == "N" or jouer_jeu == "n":
        print(f"Vous repartez avec un total de {score} points !\nMerci d'avoir joué et à bientôt !")
        exit()  # Arrêter immédiatement l'exécution du script Python

def recuperer_nom_joueur():
     nom_joueur = input("Merci de saisir votre nom:")
     nom_joueur = nom_joueur.capitalize()
     if not nom_joueur.isalpha() or len(nom_joueur) < 4:
        print("Le nom que vous avez saisi est invalide")
        return recuperer_nom_joueur()
     else:
        return nom_joueur


# Fonction principale contenant toute la logique du jeu du pendu
def hangman():

    global nom_joueur
    if nom_joueur == "":
        nom_joueur = recuperer_nom_joueur()

    # Déclaration pour pouvoir modifier la variable globale 'score' définie hors de la fonction
    global score
    # Sélection du mot secret et conversion du mot en majuscules
    mot_original = choisir_mot(mots)
    mot = mot_original.upper()

    # Ensembles (sets) pour gérer les lettres uniques
    mot_lettre = set(mot)  # Ensemble des lettres restants à deviner
    alphabet = set(string.ascii_uppercase)  # Toutes les lettres de l'alphabet (A-Z)
    lettres_jouées = set()  # Historique des lettres déjà proposées
    essai = 6  # Nombre de vies ou tentatives de départ

    # Boucle du jeu : continue tant qu'il reste des lettres à trouver et des essais disponibles
    while len(mot_lettre) > 0 and essai > 0:
        # Affichage de l'état actuel : essais restants et lettres déjà jouées
        print("Vous avez", essai, "essai(s) et vous avez utilisé les lettres suivantes:", ','.join(lettres_jouées))

        # Masque le mot : affiche la lettre si elle a été devinée, sinon un underscore "_"
        mot_liste = [lettre if lettre in lettres_jouées else "_" for lettre in mot]
        print("Le mot actuel est:", ' '.join(mot_liste))

        # Saisie du joueur et conversion automatique en majuscule
        lettre_choisie = input("Entrer une lettre !").upper()

        # Cas 1 : La lettre saisie est valide (fait partie de l'alphabet) et n'a pas encore été jouée
        if lettre_choisie in alphabet - lettres_jouées:
            lettres_jouées.add(lettre_choisie)  # On ajoute la lettre aux lettres jouées

            # Si la lettre fait partie du mot secret
            if lettre_choisie in mot_lettre:
                mot_lettre.remove(lettre_choisie)  # On la retire des lettres à deviner
                essai = 6  # Réinitialise le nombre d'essais à 6 après chaque bonne lettre
            else:
                essai -= 1  # Mauvaise lettre : on perd 1 essai
                print("Il vous reste", essai, "essai(s)")

        # Cas 2 : La lettre a déjà été proposée précédemment
        elif lettre_choisie in lettres_jouées:
            print(nom_joueur,"vous avez déjà utilisé cette lettre, choisissez une autre lettre!")

        # Cas 3 : La saisie est invalide (chiffre, symbole ou plusieurs caractères)
        else:
            print("Votre choix est incorrecte, merci de choisir une lettre!")

    # Fin de la partie : vérification de la raison de sortie de boucle
    if essai == 0:
        print(f"{nom_joueur} vous avez perdu avec un total de: {score} points.\nIl ne vous reste plus d'essai!")
        jouer_de_nouveau() # Appelle la fonction pour proposer de relancer une partie
    else:
        print(f"Le mot à deviner est {mot}. Félicitations {nom_joueur}, vous avez gagné 10 points!")

        # Ajout de 10 points au score global en cas de victoire
        score += 10
        print(nom_joueur, f"votre score est de: {score} points!") # Affichage du nouveau score cumulé
        jouer_de_nouveau() # Appelle la fonction pour proposer de relancer une partie

hangman()

