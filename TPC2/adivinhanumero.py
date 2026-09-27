import random

def modalidade1 ():
    numerocerto = random.randint (0,100)
    palpite = int(input ("Escolhe um número de 0 a 100"))
    tentativas = 1
    while palpite != numerocerto:
        if palpite == numerocerto:
            print (f"acertou em {tentativas} tentativas")
        else:
            if palpite < numerocerto:
                print ("o número que pensei é maior")
            else:
                print ("o número que pensei é menor")
        palpite = int(input ("Escolhe um número de 0 a 100"))
        tentativas = tentativas + 1
    print (f"Acertou em {tentativas} tentativas.")

def modalidade2 ():
    min = 0
    max = 100 
    tentativas = 1
    print ("Pensa num número de 0 a 100")
    palpite = int((max + min)/2)
    print(f"Pensei no número {palpite}")
    resposta = input("Responde (certo / maior / menor): ")
    
    while resposta != "certo":
        tentativas = tentativas + 1 
        if resposta == "menor":
            max = palpite - 1
        else:    
            if resposta == "maior":
                min = palpite + 1
        palpite = int((max + min)/2)
        print(f"A minha resposta é {palpite}")
        resposta = input("Responde (certo / maior / menor): ")
    print (f"Acertei em {tentativas} tentativas!")
   
modalidade = input("Escolhe a modalidade: 1 - tu adivinhas ou 2 - o computador adivinha.")
if modalidade == "1":
    modalidade1()
else:
    modalidade2()

