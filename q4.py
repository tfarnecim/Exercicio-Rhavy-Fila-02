from random import randint

def enfileira(fila,v):
    fila.append(v)
    return fila

def desenfileira(fila):
    fila.pop(0)
    return fila
    
fila_pessoas = []
for i in range(1000):
    fila_pessoas = enfileira(fila_pessoas,"PESSOA")

soma_tempo = 0
for i in range(1000):#simulando tempo que 1000 pessoas iriam esperar na fila(em minutos)
    fila_pessoas = desenfileira(fila_pessoas)
    soma_tempo += randint(1,15)

print("A MEDIA DE ESPERA FOI DE %.2f MINUTO(S) DE ESPERA"%(soma_tempo/1000))
