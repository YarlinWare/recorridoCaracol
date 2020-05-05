tamanio = int(input('Ingrese tamaño matriz: '))

valor = 0
matriz = [None]*tamanio

for i in range(0, tamanio):
    matriz[i]= [None]*tamanio

for i in range(0, tamanio):
    for j in range(0,tamanio):
        valor=valor+1
        matriz[i][j] = valor

print(matriz)

for i in range(0,tamanio):
    if (i%2 == 0):
        for j in range(0,tamanio):
            print(matriz[j][i],)
        print('')
    else:
        for j in range(tamanio-1,-1,-1):
            print(matriz[j][i],)
        print('')
