'''
O código lê uma sequência de números, permite remover o último com 0 
ou encerrar com "sair", e no final imprime a soma de todos os números registrados.
'''
lista = []
N = int(input())
for i in range(N):  # sistema de repetição
    entrada = (input())
    if entrada == "sair":
        break
 
    numero = int(entrada) #transormando o input para int

    if numero == 0:
        lista.pop()  # remoder o ultimo numero
    else:
        lista.append(numero)
soma = sum(lista)
print(soma)
