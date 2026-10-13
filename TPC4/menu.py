import random 
def CriarLista ():
    N = int (input("Introduza a quantidade de números que quer na sua lista: "))
    i = 0 
    lista = []
    while i < N:
        n = random.randint (1,100)
        lista.append (n)
        i = i + 1 
    return lista
    
def LerLista ():
    lista = []
    N = int(input ("Introduza a quantidade de números que quer na sua lista: "))
    i = 0 
    while i < N: 
        x = int (input ("Introduza o número que quer adiconar à lista: "))
        lista.append (x)
        i = i + 1 
    return lista 

def Soma (lista):
    soma = 0
    for x in lista:
        soma = soma + x 
    return soma 

def Media (lista):
    soma = 0 
    for x in lista:
        soma = soma + x 
    media = (soma/len(lista))
    return media 

def Maior (lista):
    maior = lista [0]
    for n in lista:
        if n > maior:
            maior = n 
    return maior 

def Menor (lista):
    menor = lista [0]
    for n in lista:
        if n < menor:
            menor = n 
    return menor  

def estaOrdenadacrescente (lista):
    res = True
    n = 0 
    while n < len(lista) - 1 and res == True:
        if lista [n] > lista [n + 1]:
            res = False
        n = n + 1
    return res
    

def estaOrdenadadecrescente(lista):
    res = True 
    n = 0 
    while n < len(lista) - 1 and res == True:
        if lista [n] < lista [n + 1]:
            res = False 
        n = n + 1 
    return res 
    

def Procuraelemento (lista, n):
    i = 0 
    res = -1
    while i < len(lista) and n != lista [i]:
        i = i + 1
    if i < len(lista):
        res = i 
    return res 


def menu ():
    lista = []
    mn = -1
    while mn != 0:
        print ("""
    Escolha a operação que deseja fazer:
    (1) Criar Lista 
    (2) Ler Lista
    (3) Soma
    (4) Média
    (5) Maior
    (6) Menor
    (7) estaOrdenada por ordem crescente
    (8) estaOrdenada por ordem decrescente
    (9) Procura um elemento
    (0) Sair
        """)

        mn = int(input("Escolha um número de 0-9: "))

        if mn == 1:
            lista = CriarLista ()
        elif mn == 2:
            lista = LerLista ()
        elif mn >= 3 and mn <= 9 and len(lista) == 0:
            print("Ainda não existe nenhuma lista. Use a opção 1 ou 2: ")
        elif mn == 3:
            print(f"soma = {Soma(lista)}")
        elif mn == 4:
            print (f"media = {Media(lista)}")
        elif mn == 5:
            print (f"O maior número é {Maior(lista)}")
        elif mn == 6:
            print (f"O menor número é {Menor(lista)}")
        elif mn == 7:
            if estaOrdenadacrescente(lista):
              print ("Sim")
            else:
                print ("Não")
        elif mn == 8:
            if estaOrdenadadecrescente(lista):
                print ("Sim")
            else:
                print ("Não")
        elif mn == 9:            
            n = int(input("Qual o elemento que deseja procurar? "))
            y = Procuraelemento (lista, n)
            if y == -1:
                print (f"O elemento não está na lista. Posição: {Procuraelemento(lista,n)}")
            else:
                print(f"O elemento está na posição {Procuraelemento(lista,n)}")
        elif mn == 0:
            print("Terminou de fazer operações :)")
            print (lista)


    
menu ()