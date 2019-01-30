from random import randint
import time

def desenfileirar(fila):
    fila.pop(0)

def IMPRIME(fila):
    if(len(fila)==0):
        print("NÃO HÁ NADA NA FILA DE ESPERA :/")
        return fila
    tempo = randint(1,10)
    print("IMPRIMINDO...")
    time.sleep(tempo)
    print("IMPRESSO")
    desenfileirar(fila)
    print("A IMPRESSÃO DEMOROROU %ds"%(tempo))
    return fila
    
fila = ['USER1','USER2','USER3']
fila = IMPRIME(fila)
fila = IMPRIME(fila)
fila = IMPRIME(fila)
fila = IMPRIME(fila)
