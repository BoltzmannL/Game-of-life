#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 15:25:43 2023

@author: me
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
config = input('voulez vous une génération aléatoire ?\n')
if config == 'oui':
    #taille de la grille N*N
    N=100
    #fonction génératrice de valeurs entre 0 et 1 (0 = case vide et 1 = case pleine)
    grille = np.random.choice([0,1], size=(N, N), p=[0.5,0.5])

elif config == 'non':
    edit_size = input ('quel taille grille souhaitez vous ?\n')
    N = int(edit_size)
    grille = np.zeros((N, N), dtype=int)
    pos = 0
    edit_input = input('veuillez entrer les valeurs des cases de la grille (valeurs acceptées: 1 ou 0)\n')
    for s in range ((N*N)-1):
        val_config = input()
        val_input = int(val_config)
        if val_config !=0 or val_config !=1:
            raise Exception('les seules valeurs acceptées sont 0 ou 1')
        np.insert(grille, pos, val_config)
        pos+=1
    print (grille)
    
#gestions des erreurs  
else:
    raise Exception('veuillez répondre par oui ou par non')
#règles du jeu
rule = input("quelle condition aux bords (bords clos, cylindre ou sphère) voulez vous utilisez ?\n")
if rule == 'sphère' or rule == 'bords clos' or rule == 'cylindre':
    def règle (frame_number, grille, img):
        grille_save=grille.copy()
        if rule == 'bords clos':
            for i in range (1,N-1):
                    for j in range (1,N-1):
                        compteur=(grille[i-1,j]+grille[i+1,j]+grille[i,j-1]+grille[i,j+1]+grille[i+1,j+1]+grille[i+1,j-1]+grille[i-1,j-1]+grille[i-1,j+1])
    #le compteur sert à compter le nombre de cellule voisine de la cellule à la position [i,j]        
                        if grille[i,j]==1 and (compteur<2) or (compteur>3):
                                grille_save[i,j]=0
                        elif grille[i,j] == 0 and compteur == 3:
                                    grille_save[i,j] = 1  
    #ici on verifie si la cellule [i,j] est entourée de 3 voisines, si c'est le cas et que la cellule [i,j] est vide alors elle "nait", sinon elle "meurt"
        elif rule == 'cylindre':
            for i in range (1,N-1):
                    for j in range (N):
                        compteur=(grille[i-1,j]+grille[i+1,j]+grille[i,(j-1)%N]+grille[i,(j+1)%N]+grille[i+1,(j+1)%N]+grille[i+1,(j-1)%N]+grille[i-1,(j-1)%N]+grille[i-1,(j+1)%N])     
                        if grille[i,j]==1 and (compteur<2) or (compteur>3):
                                grille_save[i,j]=0
                        elif grille[i,j] == 0 and compteur == 3:
                                    grille_save[i,j] = 1  
        elif rule == 'sphère':
          for i in range (N):
                    for j in range (N):
                        compteur=(grille[(i-1)%N,j]+grille[(i+1)%N,j]+grille[i,(j-1)%N]+grille[i,(j+1)%N]+grille[(i+1)%N,(j+1)%N]+grille[(i+1)%N,(j-1)%N]+grille[(i-1)%N,(j-1)%N]+grille[(i-1)%N,(j+1)%N])        
                        if grille[i,j]==1 and (compteur<2) or (compteur>3):
                                grille_save[i,j]=0
                        elif grille[i,j] == 0 and compteur == 3:
                                    grille_save[i,j] = 1         
        img.set_data(grille_save)
        grille[:] = grille_save[:]
        return img  
    # Création de l'animation
    fig, ax = plt.subplots()
    img = ax.imshow(grille, cmap='binary')
    ani = animation.FuncAnimation(fig, règle, fargs=(grille, img), frames=100, interval=50)    
    # Affichage de l'animation
    plt.show()
    
    
#gestions des erreurs
else:
    raise Exception('veuillez indiquer une condition aux bords valide')
