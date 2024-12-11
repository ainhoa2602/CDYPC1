lista1=0
lista2=0
for x in range(5):
    num1=int(intput("Introduce un número de la lista 1:"))
    lista1=lista1+num1

for x in range(5):
    num2=int(intput("Introduce un número de la lista2:"))
    lista2=lista2+num2

if (lista1>lista2):
    print("Lista 1 mayor")
else:
    if (lista2>lista1):
        print ("Lista 2 mayor")
    else:
        print("Listas iguales")
