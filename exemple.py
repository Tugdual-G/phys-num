# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 12:19:08 2021

@author: tugdual
"""

import numpy as np
import matplotlib.pyplot as plt

"""Création de l'enssemble des valeurs de x et de y, représentant l'espace, 
en mètres par exemple"""

x = np.linspace(-5,5,1000)
y = np.linspace(-4,4,1000)

# Création des grille d'espace X et Y:
""" Ces grilles permettent d'associer à chaque point (i,j) de 
l'espace discrètisé, son emplacement dans l'espace 'modélisé'. l'emplacement 
en x et en y est donné par X[i,j] et par Y[i,j] (ou plus simplement 
par n'importe quel point de  X[i,:] et Y[i,:]).
x est constant sur les colones de X, et y est constant sur les lignes de Y, c'est un repère
 de l'espace. Les matrices X et Y ont deux dimentions deans notre cas. 
La matrice 2d X est de la largeur de la matrice ligne x,
 et de la hauteur de y, de même pour la matrice 2d Y """

# Création des grille d'espace X et Y, grace à meshgrid:
X, Y = np.meshgrid(x,y)

"""Grace aux grilles X et Y on peut définir une fonction de deux varriables.
Les valeur de cette fonction sont stockées dans une matrice (2d)
 de même dimentions que X et Y."""
Z = np.cos(3*(X**2 + Y**2)**0.5)

"""On affiche en couleurs les valeurs de z, - vers + => sombre vers clair"""
#graph 1:
fig = plt.figure(figsize = (3,1))
ax1 = plt.subplot(1,3,1)
plt.pcolormesh(X,Y,X, cmap = 'hot', shading ='nearest')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('z = x')

#graph 2:
ax2 = plt.subplot(1,3,2)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('z = y')
plt.pcolormesh(X,Y,Y, cmap = 'hot', shading ='nearest')

#graph 3:
ax3 = plt.subplot(1,3,3)
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_title('z = cos(3*(X**2 + Y**2)**0.5)')
plt.pcolormesh(X,Y,Z, cmap = 'hot', shading ='nearest')

#marges
fig.subplots_adjust(left = 0.05, bottom = 0.1,
                       right = 0.95, top = 0.9, wspace = 0.25, hspace = 0)
