def empilhar(pilha,v):
    pilha.append(v)
    return pilha

def desenfileirar(fila):
    if(len(fila)==0):
        return fila
    fila.pop(0)
    return fila

fila = [1,2,3]
pilha = []

for i in range(len(fila)):
    pilha = empilhar(pilha,fila[0])
    fila = desenfileirar(fila)
    
for i in range(len(pilha)-1,-1,-1):
    print("%d"%(pilha[i]),end=' ')

print()
