# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 20:10:59 2022

@author: Rubenz
"""

import math

a = (float)(input("Ingrese el valor 'a' de la ecuación: "))
b = (float)(input("Ingrese el valor 'b' de la ecuación: "))
c = (float)(input("Ingrese el valor 'c' de la ecuación: "))

x_uno = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
x_dos = (-b - math.sqrt(b*b - 4*a*c))/(2*a)

print("El valor de x1 es: ",x_uno)
print("El valor de x2 es: ",x_dos)