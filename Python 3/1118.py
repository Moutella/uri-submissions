#Nome: Várias Notas Com Validação
#Resultado: Accepted
#Data: 24/07/18 20:25:07
#Linguagem: Python 3
novoCalc = 1
while(novoCalc):
    nota = -1
    nota2 = -1
    notaval = 0
    while not notaval:
        nota = float(input())
        notaval = 1
        if(nota < 0 or nota > 10):
            print("nota invalida")
            notaval = 0
    notaval = 0
    while not notaval:
        nota2 = float(input())
        notaval = 1
        if (nota2 < 0 or nota2 > 10):
            print("nota invalida")
            notaval = 0
        else:
            print("media = {:.2f}".format((nota+nota2)/2))
    print("novo calculo (1-sim 2-nao)")
    novoCalc = int(input())
    while(novoCalc!= 1 and novoCalc != 2):
        print("novo calculo (1-sim 2-nao)")
        novoCalc = int(input())
    if (novoCalc == 2):
        novoCalc = 0