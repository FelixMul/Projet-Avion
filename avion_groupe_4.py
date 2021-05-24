#Double Licence Maths Physique
#Groupe 4

# MARDAOUI YANISS
# FEDERSPIEL LUCAS
# MULLER FELIX
# LESUEUR AXEL
# BENGOCHEA BIXENTE
# BURAT JAMES

# https://github.com/FelixMul/Projet-Avion.git
#Creer les differentes parcelles: couloir, sieges
import tkinter as tk
import random as rd
import copy as cp
from operator import *


#Définir COULEURS, HAUTEUR, LARGEUR, CÔTÉ
Nombre_de_rangées = 15 #vous pouvez indiquer le nombre de rangées que vous voulez voir, mais au dela de 20 votre ordinateur peut vous poser probleme
HAUTEUR = COTE  * 7 #nous devont avoir streictement 7 lignes. 6 lignes pour les places et 1 pour le couloir
LARGEUR = Nombre_de_rangées * COTE
COTE = 40 # Taille du côté d'une parcelle
Couloir = [] #liste qui decrit les cellules du couloir [[x, y], []]
Places_dispo = [] #Liste des places libres [[x, y], []]



# Crée liste de listes où nous avons pour chaque passager
#des coordonnées (endroit où il est) et une destination (endroit où il va)
#ainsi qu'un nombre de bagage, tiré aléatoirement entre 0 et 2, de type 
#Passagers = [[coordonée_x, coordonnée_y, destination_x, destination_y, nb_baggage], ...]
Passagers = [ ]

def gen_terrain():
    """Fonction permettant de générer le terrain: 
    les listes Couloir et Places_dispo."""

    global Places_dispo
    global Couloir
    terrain.delete("all")

    for i in range(1, LARGEUR, COTE):
        for j in range(1, HAUTEUR, COTE):
            if j == HAUTEUR/2 - COTE/2 + 1:
                Couloir.append([i // COTE, j // COTE])
                terrain.create_rectangle(i, j, i+COTE, j+COTE, fill="white")
            else:
                terrain.create_rectangle(i, j, i+COTE, j+COTE, fill="grey")
                Places_dispo.append([i // COTE, j // COTE])

                
#Cette fonction serve a passer a une nouvelle etape. Elle cree un nouveau passager si la parcelle d'entree est 
#disponible et il reste des places libres. Elle sert aussi a deplacer les passagers dans l'avion.
def nouvelle_etape():
    global Passagers
    global Places_dispo

    if Passagers:
        #boucle qui deplace chaque passagers vers sa place.
        move()
        #si l'entree est libre, un nouveau passager peut arriver
        if Places_dispo:
            b = True
            for i in Passagers:
                if i[0] == 0 and i[1] == 3:
                    b = False
            if b:
                destination = rd.choice(Places_dispo)
                Places_dispo.remove(destination)
                Passagers.append([0, 3, destination[0], destination[1], rd.randint(0, 2)])
    #cela nous sert a faire entrer le premier passager               
    else:
        destination = rd.choice(Places_dispo)
        Places_dispo.remove(destination)
        Passagers.append([0, 3, destination[0], destination[1], rd.randint(0, 2)])
    
    #a la fin de l'etape nous allons dessiner l'avion et ses passagers
    for i in Couloir:
        terrain.create_rectangle(i[0] * COTE + 1, i[1] * COTE + 1 , i[0] * COTE + 1 +COTE, i[1] * COTE + 1 +COTE, fill="white")
     
    for i in Passagers:
        if i[4] == 1:
            terrain.create_oval(i[0] * COTE + 1, i[1] * COTE + 1 , i[0] * COTE + 1 +COTE, i[1] * COTE + 1 +COTE, fill="coral1")
        elif i[4] == 2:
            terrain.create_oval(i[0] * COTE + 1, i[1] * COTE + 1 , i[0] * COTE + 1 +COTE, i[1] * COTE + 1 +COTE, fill="red")
        elif i[0] == i[2] and i[1] == i[3]:
            terrain.create_oval(i[0] * COTE + 1, i[1] * COTE + 1 , i[0] * COTE + 1 +COTE, i[1] * COTE + 1 +COTE, fill="green")
        elif i[4] == 0:
            terrain.create_oval(i[0] * COTE + 1, i[1] * COTE + 1 , i[0] * COTE + 1 +COTE, i[1] * COTE + 1 +COTE, fill="blue")
        
def move():
    
    global Passagers
    """ Sort de la liste Passagers (plus grand x au début) -> mouvement de gauche a droite pour eviter les blocages
    Et plus grand y au debut au cas on a plusieurs passagers dans la meme rangée"""
    Passagers = sorted(sorted(Passagers, key = lambda x : x[0], reverse = True), key = lambda x : x[1], reverse = True)
    
    for i in Passagers:
        #on regarde d'abord si le passagers est deja arrivé dans sa rangée
        #et on doit aussi regarder si qq bloque son passage.
        if i[0] == i[2]:
            if i[4] > 0:
                i[4] -= 1
            elif i[4] == 0:
                if i[1] < i[3]:
                    i[1] += 1
                    for j in reversed(Passagers):
                        #nous devons verifier si une personne nous bloque le passage et on doit aussi
                        #savoir si cette personne est a ca place, sinon on ne peut pas changer de place avec elle.
                        if i[0:2] == j[0:2] and j != i and j[1] != j[3]:
                            i[1] -= 1
                            break
                        elif i[0:2] == j[0:2] and j != i and j[1] == j[3]:
                            j[1] -= 1
                            break
                elif i[1] > i[3]:
                    i[1] -= 1
                    for j in reversed(Passagers):
                        if i[0:2] == j[0:2] and j != i and j[1] != j[3]:
                            i[1] += 1
                            break
                        elif i[0:2] == j[0:2] and j != i and j[1] == j[3]:
                            j[1] += 1
                            break
        #si le passagers n'est pas encore dans sa rangée, nous allons juste le bouger au long du couloir
        # la variable "a" nous sert a regarder si la cellule devant le passagers est occupée
        elif i[0] != i[2]:
            a = True
            for j in Passagers:
                if j[1] == 3 and i[0] + 1 == j[0]:
                    a = False
                    break
            if a == True:
                i[0] += 1

#cette fonction est plus evidente
#elle sert a lancer une simulation via la fonction .after()
def lancer_simulation():
    nouvelle_etape()
    terrain.after(100, lancer_simulation)

#configuration de l'UI            
racine = tk.Tk()
racine.title("Simulation d'entrées de voyageurs dans un avion")

terrain = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="black")
Bouton_terrain = tk.Button(racine, text="Generate Terrain", command=gen_terrain)
Bouton_nouvelle_etape = tk.Button(racine, text = "Prochaine étape", command = nouvelle_etape)
Bouton_lancer_simulation = tk.Button(racine, text = "Lancer Simulation", command = lancer_simulation)

terrain.grid(row = 2, columnspan = 3)
Bouton_terrain.grid(row = 0, column = 0)
Bouton_nouvelle_etape.grid(row = 0, column = 1)
Bouton_lancer_simulation.grid(row = 0, column = 2)

racine.mainloop()