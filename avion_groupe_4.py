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

def gen_terrain():
    """Fonction permettant de générer le terrain. La liste Cells contient les coordonnées de chaques cellules ainsi que leurs couleurs respective, leur DUREE_FEU et DUREE_CENDRE"""

    global Cells
    Cells = []
    terrain.delete("all")

    for i in range(1, LARGEUR, COTE):
        for j in range(1, HAUTEUR, COTE):
            Cells.append([i, j, rd.choice(COULEURS), 0])
    for n in range(len(Cells)):
          if Cells[n][1] == HAUTEUR/2 - COTE/2 + 1:
               terrain.create_rectangle(Cells[n][0], Cells[n][1], Cells[n][0]+COTE, Cells[n][1]+COTE, fill="white")
          else:
               terrain.create_rectangle(Cells[n][0], Cells[n][1], Cells[n][0]+COTE, Cells[n][1]+COTE, fill="grey")

racine = tk.Tk()
racine.title("Simulation d'entrées de voyageurs dans un avion")
terrain = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="black")
Bouton_terrain = tk.Button(racine, text="Generate Terrain", command=gen_terrain)
terrain.grid(row=1, column=0)
gen_terrain()
racine.mainloop()