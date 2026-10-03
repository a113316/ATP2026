# Quem chegar ao 100 primeiro vence. O jogador e o computador vão alternadamente jogando um número de 1 a 10.

import random 

def vertente1():
        
    soma = 1
    print (f"O computador escolhe o número 1. Total: {soma}")
    while True: 
        x = int(input("Escolha um número de 1 a 10: "))
        while x < 1 or x > 10 or soma + x > 100:
            x = int(input("Número inválido. Escolhe um número de 1 a 10: "))
        print(f"O jogador escolhe o número {x}")
        soma = soma + x 
        print (f"Total: {soma}") 
        y = 11 - x 
        print (f"O computador escolhe o numero {y}")
        soma = soma + y 
        print (f"Total: {soma}")

        if soma == 100:
            print ("Fim. O computador vence! :)")
            return

def vertente2 ():
    soma = 0
    while True:
        x = int(input("Escolhe um número de 1 a 10: "))
        while x > 10 or x < 1 or soma + x > 100:
            x = int(input("Número inválido. Escolhe um número de 1 a 10: "))
        print(f"O jogador escolhe o número {x}")
        soma = soma + x
        print (f"Total: {soma}")
        if soma == 100:
            print ("Fim. Venceste :)")
            return
        y = (1 - soma ) % 11 
        if y == 0:
            y = random.randint(1,10)
        print (f"O computador escolhe o numero {y}")
        soma = soma + y 
        print (f"Total: {soma}")
        if soma == 100:
            print ("Fim. O computador vence. :)")
            return

    
vertente = input ("Escolha como quer jogar: vertente 1 - o computador começa o jogo ou vertente 2 - o jogador começa o jogo. ")

if vertente == "1":
    vertente1()
if vertente == "2":
    vertente2()