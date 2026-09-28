import random
import string
from mots import mots_courts, mots_moyens, mots_longs

score = 0
nom_joueur = ""

def choisir_mot(mots):
    mot = random.choice(mots)
    return mot

# Propose de relancer une partie ou d'arrêter le jeu
def jouer_de_nouveau():
    jouer_jeu = input("Souhaitez-vous continuer à jouer? (O = Oui, N = Non)")

    while jouer_jeu not in {"O", "o", "N","n"}:
        jouer_jeu = input("Souhaitez-vous continuer à jouer? (O = Oui, N = Non)")

    if jouer_jeu == "O" or jouer_jeu == "o":
        hangman()

    elif jouer_jeu == "N" or jouer_jeu == "n":
        print(f"Vous repartez avec un total de {score} points !\nMerci d'avoir joué et à bientôt !")
        exit()

# Demande et valide le nom du joueur (minimum 4 lettres alphabétiques)
def recuperer_nom_joueur():
     nom_joueur = input("Merci de saisir votre nom:").capitalize()
     while not nom_joueur.isalpha() or len(nom_joueur) < 4:
        print("Le nom que vous avez saisi est invalide")
        nom_joueur = input("Merci de saisir votre nom:").capitalize()
     return nom_joueur


# Fonction principale contenant toute la logique du jeu du pendu
def hangman():

    global nom_joueur
    if nom_joueur == "":
        nom_joueur = recuperer_nom_joueur()

    global score

    # Options : Choix du niveau de difficulté ---
    print("\nChoisissez un niveau de difficulté :")
    print("1 - Facile (mots courts)")
    print("2 - Moyen (mots moyens)")
    print("3 - Difficile (mots longs)")

    choix = input("Entrez votre choix (1, 2 ou 3) : ")
    while choix not in {"1", "2", "3"}:
        choix = input("Choix invalide. Merci d'entrer 1, 2 ou 3 : ")

    if choix == "1":
        liste_mots = mots_courts
    elif choix == "2":
        liste_mots = mots_moyens
    else:
        liste_mots = mots_longs

    # Sélection du mot dans la liste correspondant à la difficulté choisie
    mot_original = choisir_mot(liste_mots)
    mot = mot_original.upper()

    # Ensembles (sets) pour suivre les lettres restant à deviner et proposées
    mot_lettre = set(mot)
    alphabet = set(string.ascii_uppercase)
    lettres_jouées = set()
    essai = 6

    while len(mot_lettre) > 0 and essai > 0:
        print("Vous avez", essai, "essai(s) et vous avez utilisé les lettres suivantes:", ','.join(lettres_jouées))

        # Masque le mot secret avec des underscores
        mot_liste = [lettre if lettre in lettres_jouées else "_" for lettre in mot]
        print("Le mot actuel est:", ' '.join(mot_liste))

        lettre_choisie = input("Entrer une lettre !").upper()

        if lettre_choisie in alphabet - lettres_jouées:
            lettres_jouées.add(lettre_choisie)

            if lettre_choisie in mot_lettre:
                mot_lettre.remove(lettre_choisie)

            else:
                essai -= 1
                print("Il vous reste", essai, "essai(s)")

        elif lettre_choisie in lettres_jouées:
            print(f"{nom_joueur}, vous avez déjà utilisé cette lettre, choisissez une autre lettre!")

        else:
            print("Votre choix est incorrecte, merci de choisir une lettre!")

    # Condition de fin de partie
    if essai == 0:
        print(f"{nom_joueur} vous avez perdu avec un total de: {score} points.\nIl ne vous reste plus d'essai!")
        jouer_de_nouveau()
    else:
        print(f"Le mot à deviner est {mot}. Félicitations {nom_joueur}, vous avez gagné 10 points!")

        score += 10
        print(nom_joueur, f"votre score est de: {score} points!")
        jouer_de_nouveau()

hangman()