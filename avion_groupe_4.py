#Double Licence Maths Physique
#Groupe 4

# MARDAOUI YANISS
# FEDERSPIEL LUCAS
# MULLER FELIX
# LESUEUR AXEL
# BENGOCHEA BIXENTE
# BURAT JAMES

# https://github.com/FelixMul/Projet-Avion.git
#Creer les differentes parcelles: couloir, sieges. - AXEL
import tkinter as tk
import random as rd
import copy as cp


#Définir COULEURS, HAUTEUR, LARGEUR, CÔTÉ
HAUTEUR = 280
LARGEUR = 1200
COTE = 40 # Taille du côté, doit être un diviseur commun de la largeur et de la hauteur
COULEURS = ["white","grey"]
Places = []
Couloir = []
Passagers = []
Places_dispo = []



""" Crée liste de listes où nous avons pour chaque passager
des coordonnées (endroit où il est) et une destination (endroit où il va)
ainsi qu'un nombre de bagage tiré aléatoirement entre 1 et 2 de type 
Passagers = [[coordonée_x, coordonnée_y, destination_x, destination_y, nb_baggage], ...]"""
Passagers = [ ]

def gen_terrain():
    """Fonction permettant de générer le terrain. La liste Couloir
    contient les coordonnées de chaques cellules du couloir et ses couleurs et la liste Places 
    contient les coordonnées des places disponibles"""

    global Places_dispo
    global Couloir
    global Places
    terrain.delete("all")

    for i in range(1, LARGEUR, COTE):
        for j in range(1, HAUTEUR, COTE):
            if j == HAUTEUR/2 - COTE/2 + 1:
                Couloir.append([i, j, "white"])
                terrain.create_rectangle(i, j, i+COTE, j+COTE, fill="white")
            else:
                terrain.create_rectangle(i, j, i+COTE, j+COTE, fill="grey")
                Places.append([i, j, "grey"])
                
    Places_dispo = cp.deepcopy(Places)
                
#Cette fonction serve a passer a une nouvelle etape. Elle cree un nouveau passager si la parcelle d'entree est 
#disponible et il reste des places libres. Elle sert aussi a deplacer les passagers dans l'avion.
def nouvelle_etape():
    global Passagers, Couloir
    global Places_dispo

    move()
    #boucle qui deplace chaque passagers vers sa place.
    if len(Places_dispo) > 0 and Couloir[0][2] == "white":
        destination = rd.choice(Places_dispo)
        Places_dispo.remove(destination)
        Passagers.append([Couloir[0][0], Couloir[0][1], destination[0], destination[1], rd.randint(0, 2)])
        print(Passagers)
    
    nb_passager = 0

    for i in range(len(Passagers)):
        if Passagers[i][0] == Couloir[0][0] and Passagers[i][1] == Couloir[0][1]:
            Couloir[0][2] = "blue"
        else:
            nb_passager += 1
    
    if nb_passager == len(Passagers):
        Couloir[0][2] = "white"

    print(Couloir[0])

    terrain.after(40, nouvelle_etape)


### Sort de la liste Passagers (plus grand x au début) -> mouvement de gauche a droite pour eviter les blocages

def move():

    global Passagers

    terrain.delete("all")

    for i in range(1, LARGEUR, COTE):
        for j in range(1, HAUTEUR, COTE):
            if j == HAUTEUR/2 - COTE/2 + 1:
                terrain.create_rectangle(i, j, i+COTE, j+COTE, fill="white")
            else:
                terrain.create_rectangle(i, j, i+COTE, j+COTE, fill="grey")

    sort_list(Passagers)
    for i in range(len(Passagers)):
        n = 0
    
        if Passagers[i][0] < Passagers[i][2]:

            for j in range(len(Passagers)):
                if Passagers[i][1] == Couloir[0][1] and Passagers[i][0] + COTE == Passagers[j][0] and Passagers[j][1] == Couloir[0][1]:
                    n += 1


                elif Passagers[i][1] == Couloir[0][1] and Passagers[i][0] + COTE != Passagers[j][0]:
                    pass
            
            if n >= 1:
                pass

            elif n == 0 and Passagers[i][0] <= Passagers[i][2]:
                Passagers[i][0] += COTE

        elif Passagers[i][0] == Passagers[i][2] and Passagers[i][4] > 0:

            Passagers[i][4] -= 1

        elif Passagers[i][0] == Passagers[i][2] and Passagers[i][4] == 0 and Passagers[i][1] != Passagers[i][3]:

            if Passagers[i][1] < Passagers[i][3]:
                bloque = False
                for k in range(len(Passagers)):

                    if Passagers[i][1] + COTE == Passagers[k][1] and Passagers[i][0] == Passagers[k][0]:
                        Passagers[i][1] += COTE
                        Passagers[k][1] -= COTE
                        bloque = True

                if bloque == False:
                    Passagers[i][1] += COTE
                    

            elif Passagers[i][1] > Passagers[i][3]:
                bloque = False
                for k in range(len(Passagers)):

                    if Passagers[i][1] - COTE == Passagers[k][1] and Passagers[i][0] == Passagers[k][0]:
                        Passagers[i][1] -= COTE
                        Passagers[k][1] += COTE
                        bloque = True

                if bloque == False:
                    Passagers[i][1] -= COTE
                    

    

    for a in range(len(Passagers)):
        terrain.create_oval(Passagers[a][0], Passagers[a][1], Passagers[a][0] + COTE, Passagers[a][1] + COTE, fill="blue")



def sort_list(liste):
    """Permet de trier les éléments d'une liste selon les coordonées x de facons décroissante"""

    liste.sort(key = lambda x : x[0])
    liste.reverse()


                
                
racine = tk.Tk()
racine.title("Simulation d'entrées de voyageurs dans un avion")

terrain = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="black")
Bouton_terrain = tk.Button(racine, text="Generate Terrain", command=gen_terrain)
Bouton_nouvelle_etape = tk.Button(racine, text = "Prochaine étape", command = nouvelle_etape)

terrain.grid(row = 2, columnspan = 2)
Bouton_terrain.grid(row = 0, column = 0)
Bouton_nouvelle_etape.grid(row = 0, column = 1)

racine.mainloop()