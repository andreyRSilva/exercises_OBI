'''
O código lê os resultados de 6 partidas de um grupo, conta quantas vitórias ele teve e o classifica 
em uma categoria de desempenho de acordo com a quantidade de vitórias.
'''

#armazenando
vitorias = []
#nome = str(input())

#pegando os dados 
for i in range (6):
     resultado = input().upper()
     if resultado == "V":
          vitorias.append ("v")

#contagem          
ctg = len(vitorias)

#classificaçao do grupo 

if ctg >=5 :
     print("1")
elif  ctg >=3:
     print("2")
elif ctg >=1:
     print("3")
else:
     print("-1")



     

    

