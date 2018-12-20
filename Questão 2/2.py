import time
import random

def imprimir(lista):

    if(len(lista) == 0):
        print("SEM PAPEL")
        return lista

    print("COLOCANDO PAPEL...")
    
    time.sleep(random.randint(1,2))

    print("IMPRIMINDO...")

    time.sleep(random.randint(1,3))

    print("IMPRESSO")

    lista.pop(0)

    return lista

l = []

while(True):

    s = int( input("OPCOES: [1]IMPRIMIR [2]COLOCAR \n") )

    if(s==1):
        l = imprimir(l)
    elif(s==2):
        l.append(1)
        print("MAIS UMA IMPRESSAO")
















    
