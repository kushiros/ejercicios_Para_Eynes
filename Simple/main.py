# generate random integer values
import random
#los valores valor1 y valor2, son los valores de las key en cada diccionario de la lista
#de esta manera puedo utilizarlos para después ordenarlos con el bubble sort
def obtenerValue(diccionario):
    for v in diccionario.values():
        valor = ("%i" %(v))
    return valor
def diccionarioEdades():
    #creo la lista con los valores de las id
    clientes = [0,1,2,3,4,5,6,7,8,9]
    #para cada id utilizo un random generator para crear el value del diccionario que
    # va a haber en su posición
    for i in clientes:
        clientes[i] ={clientes[i]:random.randint(1,100)}
    print(clientes)
    #retorno de la lista con diccionarios estando aún desordenada
    return clientes
def ordenarDiccionario():
    diccionarioOrdenado = diccionarioEdades()
    #acá utilizo un bubble sort para ordenar la lista con diccionarios adentro
    n = len(diccionarioOrdenado)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            valor1 = obtenerValue(diccionarioOrdenado[j])
            valor2 = obtenerValue(diccionarioOrdenado[j + 1])
            if valor1 > valor2:
                swapped = True
                diccionarioOrdenado[j], diccionarioOrdenado[j + 1] = diccionarioOrdenado[j + 1], diccionarioOrdenado[j]
        if not swapped:
            return
    print(diccionarioOrdenado)
    valor1 = obtenerValue(diccionarioOrdenado[0])
    valor2 = obtenerValue(diccionarioOrdenado[9])
    print(valor1)
    print(valor2)

ordenarDiccionario()

