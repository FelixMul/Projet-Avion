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

""" Crée liste de listes où nous avons pour chaque passager
des coordonnées (endroit où il est) et une destination (endroit où il va)
ainsi qu'un nombre de bagage tiré aléatoirement entre 1 et 2 de type 
Passagers = [[coordonée_x, coordonnée_y, destination_x, destination_y, nb_baggage], ...]"""
Passagers = [ ]

def gen_terrain():
    """Fonction permettant de générer le terrain. La liste Couloir
    contient les coordonnées de chaques cellules du couloir et ses couleurs et la liste Places 
    contient les coordonnées des places disponibles"""

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
                
                
#Cette fonction serve a passer a une nouvelle etape. Elle cree un nouveau passager si la parcelle d'entree est 
#disponible et il reste des places libres. Elle sert aussi a deplacer les passagers dans l'avion.
def nouvelle_etape():
    global Passagers
    #boucle qui deplace chaque passagers vers sa place.
    if len(Places) > 0 and Couloir[0][2] == "white":
        destination = rd.choice(Places)
        Places.remove(destination)
        Passagers.append([Couloir[0][0], Couloir[0][1], destination[0], destination[1], rd.randint(0, 2)])
        
                
                
                
racine = tk.Tk()
racine.title("Simulation d'entrées de voyageurs dans un avion")

terrain = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="black")
Bouton_terrain = tk.Button(racine, text="Generate Terrain", command=gen_terrain)
Bouton_nouvelle_etape = tk.Button(racine, text = "Prochaine étape", command = nouvelle_etape)

terrain.grid(row = 2, columnspan = 2)
Bouton_terrain.grid(row = 0, column = 0)
Bouton_nouvelle_etape.grid(row = 0, column = 1)

racine.mainloop()