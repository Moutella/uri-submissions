#Nome: Abaixo da Diagonal Principal
#Resultado: Accepted
#Data: 25/07/18 13:38:14
#Linguagem: Python 3
op = input()
matriz = []
for i in range(0,12):
    matriz.append([])
    for j in range(0, 12):
        matriz[i].append(float(input()))

soma = 0
for k in range(0, 12):
    for j in range(0,k):
        soma+= matriz[k][j]

if(op=="S"):
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/66))
