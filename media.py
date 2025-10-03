import pandas as pd

x=[20,20,20,20,40]
media=sum(x)/len(x)
print(media)

"""
Média aritmética ponderada
soma(dados * pesos) soma(pesos)
"""
pesos=(1,2,3,4)
notas=(8,7,9,9)

notasXpesos=[notas[1] * pesos[1] for i in range(0,len(notas))]
print(notasXpesos)

somaNotasXpesos=sum(notasXpesos)
mediaPonderada=somaNotasXpesos/sum(pesos)
print(mediaPonderada)