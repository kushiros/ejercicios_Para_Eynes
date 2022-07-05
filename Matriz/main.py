import random
"""Nombre: Matriz
Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final.
"""
def matrizRandomizada():
    matriz = []
    for i in range(5):
        matriz.append([])
        for j in range(5):
            matriz[i].append(random.randint(1,5))
    return matriz

def encontrar4ConsecutivosVertical(matriz):
    matrizbusca = matriz
    for i in range(4):
        valor=True
        contador=0
        for j in range(4):
            if ((matrizbusca[i][j])==(matrizbusca[i][j+1]-1) and valor==True):
                contador+=1
            else:
                valor=False
                contador=0
            if(contador==4):
                return(valor)
    if(valor==False):
        return valor

def encontrar4ConsecutivosHorizontal(matriz):
    matrizbusca = matriz
    for i in range(4):
        valor=True
        contador=0
        for j in range(4):
            if ((matrizbusca[j][i])==(matrizbusca[j+1][i]-1) and valor==True):
                contador+=1
            else:
                valor=False
                contador=0
            if(contador==4):
                return(valor)
    if(valor==False):
        return valor
matriz = matrizRandomizada()
print(matriz)
print(encontrar4ConsecutivosHorizontal(matriz))
print(encontrar4ConsecutivosVertical(matriz))
matrizConVerticalConsecutivo = [[1, 3, 1, 4, 5], [2, 5, 5, 1, 5], [3, 5, 5, 3, 1], [4, 4, 4, 4, 4], [5, 1, 5, 1, 1]]
print(encontrar4ConsecutivosHorizontal(matrizConVerticalConsecutivo))
print(encontrar4ConsecutivosVertical(matrizConVerticalConsecutivo))
matrizConHorizontalConsecutivo = [[1 ,2, 3 ,4 ,5], [4, 2, 2, 4, 1], [3, 4, 4, 4, 3], [3, 3, 2, 1, 1], [5, 5, 1, 5, 3]]
print(encontrar4ConsecutivosHorizontal(matrizConHorizontalConsecutivo))
print(encontrar4ConsecutivosVertical(matrizConHorizontalConsecutivo))