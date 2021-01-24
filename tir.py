# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:43:28 2021

@author: tugdual

Lancé d'une balle avec du vent
"""
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, pi

# Gravité
g = 10

# Constantes liées aux frottements.
m = 1
rho = 1.22
C_x = 0.5
S = 0.1
C = 1/(2*m)*S*C_x*rho

# Vent:
wind = - 10


# Temps total d'intégration:
t_max = 3.5

# Itervalle de temps pour l'intégration:
# Le shéma d'Euler est imprécis à l'ordre 1, 
# ça se constate en augmentant la valeur de dt.
dt = 0.001

# Interval d'enregistrement de chaque image.
Delta_t = dt*10

# Création des listes de vitesses et de temps
t = np.arange(1, t_max+Delta_t, Delta_t)
v_x = np.empty((len(t)))
v_y = np.empty((len(t)))

# Conditions initiales
v_init = 20.
alph = pi/4

v_x[0] = v_init*cos(alph) 
v_y[0] = v_init*sin(alph)

v_x0 = v_x[0]
v_y0 = v_y[0]

dv_y = 0.
dv_x = 0.

x = np.empty((len(t)))
y = np.empty((len(t)))

# On lance la balle à partir de (0,0):
x[0] = 0
y[0] = 0

# X_Dt : Déplacement de la balle entre chaque itération de la boucle 1
# initialisation:
x_Dt = 0
y_Dt = 0

#Résolution de l'équation diff:
for i in range(len(t)-1):
    # Intégration de l'équation sur le temps Delta_t:
    x_Dt = 0
    y_Dt = 0
    for j in range(int(Delta_t/dt)):
        
        #Variation de la vitesse:
        dv_x = -C*(v_x0 - wind)*np.abs(v_x0 - wind)        
        dv_y = -(g + C*v_y0*np.abs(v_y0)) 
        
        # vitesse après l'écoulement du temps dt:
        v_x0 = v_x0 + dv_x*dt
        v_y0 = v_y0 + dv_y*dt
        
        # Ajout du déplacement après dt:
        y_Dt += dt*v_y0
        x_Dt += dt*v_x0
       
    # Stockage de la valeur de la vitesse 
    v_y[i+1] = v_y0
    v_x[i+1] = v_x0
    
    # Stockage des positions
    x[i+1] = x[i] + x_Dt
    y[i+1] = y[i] + y_Dt



plt.figure(dpi = 200)
plt.scatter(x, y, s = 2, marker = '.', c = (v_x**2 + v_y**2)**0.5, cmap = 'hot')

plt.annotate('Départ', xy = (x[0],y[0]), xytext=(0,0),
                 textcoords = 'offset points', color = 'black')

plt.annotate('Arrivée', xy = (x[len(x)-1],y[len(y)-1]), xytext=(-10,0),
                 textcoords = 'offset points', color = 'black')
plt.xlabel('L (m)')
plt.ylabel('H (m)')
plt.legend()
plt.grid()
plt.show()
