matriz=[[1,2,3][4,5,6][7,8,9]] #[1,2,3][8,9,4][7,6,5]

def girar(matriz):
    return [[x[y] for x in matriz] for y in range(-1,((len(matriz[0])+1)*-1),-1)]

def caracol(lista, matriz):
    if len(matriz) <=1:
        return lista + matriz[0]
    return caracol(lista+matriz[0].girar(matriz[1:]))
