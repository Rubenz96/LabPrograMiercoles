# from funciones import calcularPromedio as calc

from funciones import calculaLogaritmoUno 
from funciones import calculaLogaritmoDos 
from funciones import calcularPromedio

# valor = calculaLogaritmoUno(argumento=8,base=2)
# print(valor)
#########################################################
# valor = calculaLogaritmoDos(argumento=8,base=2)
# print(valor)

# valor = calculaLogaritmoDos(base=2)
# print(valor)

# valor = calculaLogaritmoDos(argumento=8)
# print(valor)

# valor = calculaLogaritmoDos()
# print(valor)

#########################################################
nota_uno = 4
nota_dos = 7
nota_tres = 10


valor = calcularPromedio(x=nota_uno,y=nota_dos,z=nota_tres)
print(valor)

valor = calcularPromedio(y=nota_dos,z=nota_tres)
print(valor)

valor = calcularPromedio(z=nota_tres)
print(valor)

valor = calcularPromedio()
print(valor)

valor = calcularPromedio(x=nota_uno,z=nota_tres)
print(valor)

valor = calcularPromedio(x=nota_uno,y=nota_dos)
print(valor)

valor = calcularPromedio(x=nota_uno)
print(valor)

valor = calcularPromedio(y=nota_dos)
print(valor)

