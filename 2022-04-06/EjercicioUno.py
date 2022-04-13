# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 20:15:39 2022

@author: Rubenz
"""

import math


raiz = math.sqrt(16)
print(raiz)

#True equivale a 1
raiz = math.sqrt(True)
print(raiz)

#False equivale a 0
raiz = math.sqrt(False)
print(raiz)

#Genera un error, porque no permite numeros negativos
raiz = math.sqrt(-16)
print(raiz)
