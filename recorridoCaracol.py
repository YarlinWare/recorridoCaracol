tamanio = int(input('Ingrese tamaño matriz: '))

matriz=[]
a = 0
b = tamanio - 1
valor = 0
i=0
j=0


for i in range(tamanio):

    for j in range(b):
        valor=[valor+1]*b
        matriz.append(valor)

    for k in range(1,b):
        valor=[valor+1]*b
        matriz.append(valor)

for i in tamanio:
    for j in range(matriz[i]):
        print(matriz[i][j])

