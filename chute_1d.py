# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 19:21:58 2021

@author: tugdual

Chute d'un objet, shéma le plus simple d'Euler en temps <=> RK d'ordre 1.
Chute en 1 dimension.
"""
import numpy as np
import matplotlib.pyplot as plt

g = 10
m = 1
rho = 1.22
C_x = 0.5
S = 0.1
C = 1/(2*m)*S*C_x*rho

# temps écoulé entre chaque valeur enregistrée de la vitesse 
Delta_t = 0.1

# Temps total d'intégration:
t_max =8

# Itervalle de temps pour l'intégration:
# Le shéma d'Euler est imprécis à l'ordre 1, 
# ça se constate en augmentant la valeur de dt.
dt = 0.001

t = np.arange(1, t_max+Delta_t, Delta_t)
v = np.empty((len(t)))

# Condition initiale
v[0] = 0
v_0 = 0
v_1 = 0

for i in range(len(t)-1):
    # Intégration de l'équation sur le temps Delta_t:
    for j in range(int(Delta_t/dt)):        
        dv = -(g + C*v_0*np.abs(v_0))
        v_1 = v_0 + dv*dt
        v_0 = v_1
    # Stockage de la valeur de la vitesse 
    v[i+1] = v_1
    
plt.plot(t,v)
plt.xlabel('temps en secondes')
plt.ylabel('vitesse en m/s')
plt.grid()
plt.show()