#Nome: Área Esquerda
#Resultado: Wrong answer (100%)
#Data: 25/07/18 14:01:30
#Linguagem: Python 3
op = input()
matriz = []
for i in range(0,12):
    matriz.append([])
    for j in range(0, 12):
        matriz[i].append(float(input()))

soma = 0
for k in range(0,6):
    for j in range(-(k-6),k-6):
        soma+= matriz[j+6][k]

if(op=="S"):
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/30))
