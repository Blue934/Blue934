
import random

x =['anticonstitutionnellement', 'synopsys', 'obliterer']
y =['cinematique', 'figure', 'chance'] 
z =['celibataire','analogue','hypertension']

def Gameover(point_T):
    print(f"La partie est terminée, vous avez collecté {point_T} bonne reponse !")
    if point_T <= 3:
        print("Vous etes nul !")
    elif point_T >= 4 and point_T <=6:
        print("Pas si mal !")
    elif point_T >= 7 and point_T <= 8:
        print("Tres bien joué !")
    else:
        print("Exellent !")

def listdepart(liste):  
    list_depart = []                                     #liste dans laquel je vais stocker mes lettre non double
    for element in range(len(liste)):                    #Pour chaque element de ma liste
        mot = liste[element]                             #Le mot est = a l'element de ma liste indexe au numero de l'iterateur
        mot_copy = mot
        for i in range(len(mot)):                        #Pour chaque lettre dans mon mot
            lettre = mot_copy[i]                         #Une lettre correspondant a l'indice de l'iterateur
            if lettre in list_depart:                    #Si cette lettre est deja presente dans ma liste_final pas d'ajoute
            #print("Suppression du doublon")
                pass
            else:                                        #sinon ajout a la liste
                alea = random.randint(0, len(mot) - 1)   #Un chiffre aleatoire compris entre 0 et la taille max du mot - 1
                list_depart.insert(alea, lettre)
    print("Voici votre liste de depart.")
    print (list_depart)
    print("Taille:", len(list_depart))
    return list_depart

def mchoix (check1, check2, check3, GameOver, point_T):
    if check1 == True and check2 == True and check3 == True:
        GameOver = True
    else:
        GameOver = False
    print("Il y 3 manche [premiere, deuxieme et troisieme], chacune de ces manche comporte 3 mots qui valent 1 point avec une difficulté ascendante !")
    print("Enter votre le chiffre en lettre ou '''j'ai fini''' pour arreter la partie :")
    print("Quelle manche avez vous choisis ?")
    choix = input("ex. un ou deux ou trois:\n")
    if choix.lower() == "un" and check1 == False:
        m = 1
        return m, GameOver
    elif choix == "deux" and check2 == False:
        m = 2
        return m, GameOver
    elif choix.lower() == "trois" and check3 == False:
        m = 3
        return m, GameOver
    elif choix.lower() == "j'ai fini":
        print("A bientot !")
        GameOver = True
        Gameover(point_T)
        m = 0
        return m, GameOver
    elif choix.lower() == "un" and check1 == True or choix.lower() == "deux" and check2 == True or choix.lower() == "trois" and check3 == True:
        print("Vous 'avez plus accés a cette manche !")
        m = "reset"
        return m, GameOver


def manche(manche_nb, point_T, mot_trouve, check1, check2, check3, interruption, GameOver, m, end):
    m = m
    point = 0
    tentatives = 30
    GameOver = GameOver
    while not GameOver:
        if manche_nb == 1 and check1 == False:
            liste_depart = listdepart(z)
        elif manche_nb == 2  and check2 == False:
            liste_depart = listdepart(y)
        elif manche_nb == 3 and check3 == False:
            liste_depart = listdepart(x)
        elif check1 == True and check2 == True and check3 == True:
            break
        elif manche_nb == 0:
            print("Merci d'avoir joué !" )
            end = True
            break
        elif manche_nb == 'reset': 
            mchoix(check1, check2, check3, GameOver, point_T)
        else:
            print("Une erreur est survenue lors de l'attribution de la bonne liste pour cette manche!")
            break
        print("Enter un des 3 mot que vous pensé avoir trouvée ou entrer le mot stop pour changer de manche a tout moment !")
        reponse = input("Bonne Chance:\n")
        ################################# I MANCHE ##################################################
        if manche_nb == 1:
            if reponse.lower() in z and reponse.lower() not in mot_trouve:
                print(f"Vous avez trouvée le mot : {reponse}")
                mot_trouve.append(reponse)
                point += 1 
                point_T += 1
                tentatives -= 1 
                if point == 3 and point_T == 9:
                    print("Vous avez complété totalement le jeu ! Félicitation")
                    check1 = True
                    Gameover(point_T)
                    break
                elif point == 3 and point_T != 9:
                    print("Vous avez complété totalement la manche 1 ! Félicitation")
                    print(f"Vous avez {point_T} point !")
                    print("Bonus tentatives + 3")
                    print("Attention à partir de ce stade je ne vous informerez que lorque vous trouvé un mot , le changement de manche devra ce faire manuellement une fois les 3 mots trouvés ;)  ")
                    tentatives += 3 
                    check1 = True
                    
                    liste_depart.clear()
                    #print(f"Voici la liste dne depart ;\n {liste_depart}")
                    m, GameOver = mchoix(check1, check2, check3, GameOver, point_T)
                    manche_nb = m
                    continue
                else:
                    print(f"Il vous reste {tentatives} tentative")
                    tentatives -= 1
                    if tentatives == 0:
                        print(f"Vous avez perdu ! Vous avez {point_T} point")
                        liste_depart.clear()
                        GameOver = True
                        break
            elif reponse.lower() == "stop":
                print("Les mots deja trouvé ont été sauvegardé")
                interruption = True
                break
        ################################# II MANCHE  ####################################################
        elif manche_nb == 2:
            if reponse.lower() in y and reponse.lower() not in mot_trouve:
                print(f"Vous avez trouvée le mot : {reponse}")
                mot_trouve.append(reponse)
                point += 1 
                point_T += 1
                tentatives -= 1 
                if point == 3 and point_T == 9:
                    print("Vous avez complété totalement le jeu ! Félicitation")
                    check2 = True
                    Gameover(point_T)
                    break
                elif point == 3 and point_T != 9:
                    print("Vous avez complété totalement la manche 2 ! Félicitation")
                    print(f"Vous avez {point_T} point !")
                    print("Bonus tentatives + 3")
                    tentatives += 3 
                    check2 = True
                    liste_depart.clear()
                    #print(f"Voici la liste dne depart ;\n {liste_depart}")
                    m, GameOver = mchoix(check1, check2, check3, GameOver, point_T)
                    manche_nb = m
                    continue
                else:
                    print(f"Il vous reste {tentatives} tentative")
                    tentatives -= 1
                    if tentatives == 0:
                        print(f"Vous avez perdu ! Vous avez {point_T} point")
                        liste_depart.clear()
                        GameOver = True
                        break
            elif reponse.lower() == "stop":
                    print("Les mots deja trouvé ont été sauvegardé")
                    interruption = True
                    break
        ########################### III MANCHE ###########################################
        elif manche_nb == 3:
            if reponse.lower() in x and reponse.lower() not in mot_trouve:
                print(f"Vous avez trouvée le mot : {reponse}")
                mot_trouve.append(reponse)
                point += 1 
                point_T += 1
                tentatives -= 1 
                if point == 3 and point_T == 9:
                    print("Vous avez complété totalement le jeu ! Félicitation")
                    check3 = True
                    Gameover(point_T)
                    break
                elif point == 3 and point_T != 9:
                    print("Vous avez complété totalement la manche 3 ! Félicitation")
                    print(f"Vous avez {point_T} point !")
                    print("Bonus tentatives + 3")
                    tentatives += 3 
                    check3 = True
                    liste_depart.clear()
                    #print(f"Voici la liste dne depart ;\n {liste_depart}")
                    m, GameOver = mchoix(check1, check2, check3, GameOver, point_T)
                    manche_nb = m
                    continue
                else:
                    print(f"Il vous reste {tentatives} tentative")
                    tentatives -= 1
                    if tentatives == 0:
                        print(f"Vous avez perdu ! Vous avez {point_T} point")
                        liste_depart.clear()
                        GameOver = True
                        break
            elif reponse.lower() == "stop":
                print("Les mots deja trouvé ont été sauvegardé")
                interruption = True
                break
        else:
            print("Une erreur est survenue lors du choix entre les 3 manches!")
            break
    #fin de boucle
    return mot_trouve, GameOver, point_T, check1, check2, check3, interruption, m, manche_nb, end

#variable au top depart
point_T = 0
mot_trouve = []
interruption = False
GameOver = False
check1 = False
check2 = False
check3 = False
end = False

# Fichier main () deroulement du jeu #
while not check1 and not check2 and not check3:
    m, GameOver = mchoix(check1, check2, check3, GameOver, point_T)
    manche_nb = m 
    mot_trouve, GameOver, point_T, check1, check2, check3, interruption, m, manche_nb, end = manche(manche_nb, point_T, mot_trouve, check1, check2, check3, interruption, GameOver, m, end)
    if interruption:
        m, GameOver = mchoix(check1, check2, check3, GameOver, point_T)
        manche_nb = m
        mot_trouve, GameOver, point_T, check1, check2, check3, interruption, m, manche_nb, end = manche(manche_nb, point_T, mot_trouve, check1, check2, check3, interruption, GameOver, m, end)
        if end:
            break