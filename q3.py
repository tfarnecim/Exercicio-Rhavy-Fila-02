from random import randint

def enfileira(fila,v):
    fila.append(v)
    return fila

#minuto em que o i-ésimo cliente foi atendido logo após a abertura do centro de atendimento
#cada cliente deve ser atendido imediatamente após o outro
tempos = []
#por simplicidade o nome dos clientes segue um padrão
clientes = []

tempo_at = 0
sum = 0

for i in range(1000):
    tempos = enfileira(tempos,tempo_at)
    clientes = enfileira(clientes,'a')
    aux = randint(1,15)#cada cliente leva até 15 minutos para ser atendido
    tempo_at += aux
    sum += aux

print("TEMPO MEDIO: %.2f"%(sum/1000))
#nomes e minutos em que cada cliente é atendido são guardados em 'clientes' e 'tempos' respectivamente
