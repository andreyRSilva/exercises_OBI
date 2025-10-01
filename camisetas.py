'''
O código confirma se a distribuição de camisetad para os 
alunos nas categorias "1" e "2" bate exatamente com os números fornecidos.
'''
nca = int(input())
ta = (input())
p = int(input())
m = int(input())
tp = ta.count("1")
tm = ta.count("2")
total = p + m


if nca == total and p == tp and m == tm:
    print("S")
else :
    print("N")


