'''
O código verifica se é possível transformar A em um anagrama de P, 
usando os asteriscos como letras coringa para completar as que faltam.
'''
from collections import Counter

# Leitura das palavras
P = input()
A = input()

# Conta as letras de cada palavra
contadorP = Counter(P)
contadorA = Counter(c for c in A if c != '*')
quantidade_asteriscos = A.count('*')

# Calcula o total de letras que faltam em A para virar um anagrama de P
faltando = 0
for letra in contadorP:
    qtd_P = contadorP[letra]
    qtd_A = contadorA.get(letra, 0)
    if qtd_A < qtd_P:
        faltando += qtd_P - qtd_A

# Verifica se os asteriscos conseguem cobrir o que está faltando
if faltando <= quantidade_asteriscos:
    print("S")
else:
    print("N")

