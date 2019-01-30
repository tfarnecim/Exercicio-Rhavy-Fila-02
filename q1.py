def empilhar(pilha,v):
    pilha.append(v)
    return pilha

def desenfileirar(fila):
    if(len(fila)==0):
        return fila
    fila.pop()
    return fila

def front(fila):
    return fila[len(fila)-1]

fila = ['A','B','A','C','A','X','I']
pilha = []

for i in range(len(fila)):
    pilha = empilhar(pilha,front(fila))
    fila = desenfileirar(fila)

for i in range(len(pilha)):
    print(pilha[i],end='')
