#Nome: Matriz Quadrada III
#Resultado: Runtime error
#Data: 25/07/18 21:50:38
#Linguagem: Python 3
import math
while 1:
    entrada = int(input())
    if entrada == "0":
        break
    caracteres = 1
    x = 2 ** (entrada*2)
    car = entrada
    while x >= 10:
        x/=10
        caracteres+=1
    for i in range(0, entrada):
        for j in range(0, entrada):
            valor = 2**(j+i)
            print("{0:>{x}}".format(valor, x=caracteres), end="")
            if(j!=entrada-1):
                print(" ", end="")
        print()
    print()
