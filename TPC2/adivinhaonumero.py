import random

def modo1():
    numerocerto = random.randint(0, 100)
    tentativas = 0
    acertou = False
    
    while not acertou:
        palpite = int(input("Adivinha o número (0-100): "))
        tentativas = tentativas + 1
        
        if palpite == numerocerto:
            print("Acertou")
            acertou = True
        else:
            if palpite > numerocerto:
                print("O número que pensei é Menor")
            else:
                print("O número que pensei é Maior")
    
    print(f"Acertaste em {tentativas} tentativas")


def modo2():
    minimo = 0
    maximo = 100
    tentativas = 0
    acertou = False
    
    print("Pensa num número entre 0 e 100.")
    
    while not acertou:
        palpite = (minimo + maximo) / 2
        palpite = int(palpite)
        tentativas = tentativas + 1
        print(f"O meu palpite é:{palpite}")       
        resposta = input("Responde (Acertou / Maior / Menor): ")
        
        if resposta == "Acertou":
            acertou = True
        else:
            if resposta == "Maior":
                minimo = palpite + 1
            else:
                maximo = palpite - 1
    
    print("Acertei em", tentativas, "tentativas")


modalidade = input("Escolhe a modalidade (1 - computador pensa e tu adivinhas / 2 - tu pensas e o computador adivinha): ")

if modalidade == "1":
    modo1()
else:
    modo2()
