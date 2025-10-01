# O código calcula (distância - 3) % 8 e, dependendo do resto, imprime um número específico (1, 2 ou 3) representando uma posição cíclica no acelerador.
dis = float(input())
dis2 = dis - 3
dis3 = dis2 % 8

if dis3 == 3:
    print(1)
if dis3 == 4:
    print(2)
elif dis3 == 5:
    print(3)
print(dis3)



