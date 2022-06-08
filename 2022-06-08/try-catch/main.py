
# x = 60

# try:
#     print(x)
# except:
#     print('No encontrado')


# try:
#     valor = (int)(input('Ingrese el numero: '))
# except:
#     print('Hubo un error en la ejecucion')
#     valor = 0

# print(valor)

#############################################################################

n_datos = (int)(input('Ingrese el numero de datos: '))
sumador = 0
cont = 0

while(cont < n_datos):
    try:
        numero = (int)(input('Ingrese el numero: '))
        sumador = sumador + numero
        cont = cont + 1
    except:
        print('Intente nuevamente...')

print('---------------------------------------------------------------------')
print(sumador)

















