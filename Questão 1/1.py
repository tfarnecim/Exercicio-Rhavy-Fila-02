def empilhar(pilha,v):
    pilha.append(v)
    return pilha

def desempilhar(pilha):
    if(len(pilha)==0):
        return pilha
    pilha.pop(0)
    return pilha

lista = [1,2,3]
pilha = []

for i in range(len(lista)):
    pilha.append(lista[0])
    lista.pop(0)
    
for i in range(len(pilha)-1,-1,-1):
    print("%d"%(pilha[i]),end=' ')

print()
