TabMeteo7 = [((2026,9,17), 17, 30, 0.2),((2026,9,26),19,29,0),((2026,10,21), 11, 20, 4),((2026,10,22), 8, 17, 6),((2026,10,25), 9, 16, 2)]
from matplotlib import pyplot as plt


def mediatemp ():
    res = []
    for data, tmin, tmax, prec in TabMeteo7:
        media = (tmin + tmax)/2
        res.append ((data,media))
    return res 

def tempmin(tabMeteo):
    minima = tabMeteo [0][1]
    for data, tmin, tmax, prec in tabMeteo: 
        if tmin < minima:
            minima = tmin 
    return minima 

def amplTerm(tabMeteo):
    res = []
    for data, tmin, tmax, prec in tabMeteo: 
        amplTerm = tmax - tmin 
        res. append ((data, amplTerm))
    return res 

def maxChuva(tabMeteo):
    max_data = tabMeteo [0][0]
    max_prec = tabMeteo[0][3]
    for data, tmin, tmax, prec in tabMeteo: 
        if max_prec < prec:
            max_prec = prec 
            max_data = data        
    return (max_data, max_prec)

def diasChuvosos(tabMeteo, p):
    lista = []
    for data, tmin, tmax, prec in tabMeteo:
        if prec > p:
            lista.append ((data, prec))
    return lista  

def maxPeriodoCalor(tabMeteo, p):
    contador = 0 
    maximo = 0
    for data, tmin, tmax, prec in tabMeteo:
        if prec < p:
            contador = contador + 1 
            if contador > maximo: 
                maximo = contador 
        else: 
            contador = 0 
    return maximo  


def grafTabMeteo(t):
    y_min = [tmin for data, tmin, tmax, prec in t]
    x = [f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]
    y_max = [tmax for data, tmin, tmax, prec in t]
    y_prec = [prec for data, tmin, tmax, prec in t] 
    plt.plot (x,y_min, color = "pink", marker = "*", label = "Tmin ºC")
    plt.plot (x,y_max, color = "magenta", marker = "*", label = "Tmax ºC")
    plt.title("Temperaturas")
    plt.legend()
    plt.grid ()
    plt.show()
    plt.bar (x, y_prec, color = "lavender")
    plt.title ("Precipitação")
    plt.grid()
    plt.show ()
    return

def guardaTabMeteo(t, fnome):
    file = open (fnome, "w")
    for dia in t:
        data, tmin,tmax,prec = dia 
        ano, mes, dia = data 
        file.write(f"{ano} - {mes} - {dia} | {tmin} | {tmax} | {prec} | \n")
    file.close ()
    return

def carregaTabMeteo(fnome):
    res = []
    file = open (fnome, "r")
    for line in file:
        data,tmin,tmax, prec, _ = line.split ("|")
        ano, mes, dia = data.split ("-")
        tuplo = ((ano,mes,dia),tmin,tmax,prec)
        res.append (tuplo)
    file.close ()
    return res

def menu ():
    mn = -1 
    while mn != 0:
        print ("""
 Qual a operação que deseja fazer?
    1 - Calcular a média de temperaturas de cada dia;
    2 - Calcular a temperatura mais baixa;
    3 - Calcular a amplitude térmica de cada dia;
    4 - Calcular o valor máximo de precipitação; 
    5 - Dias com preciptação superior a p;
    6 - Número de dias consecutivos com precipitação abaixo de p;
    7 - Desenhar os gráficos de precipitação e temperatura;
    8 - Guardar a tabela meterológica em ficheiro;
    9 - Carregar a tabela metereológica de um ficheiro;
    0 - Sair da aplicação.  """)

        mn = int (input ("Opção "))

        if mn == 1:
            mediatemp ()
            print (mediatemp()) 

        elif mn == 2:
            print (tempmin (TabMeteo7))
            
        elif mn == 3: 
           print( amplTerm (TabMeteo7)) 

        elif mn == 4:
            print (maxChuva (TabMeteo7))

        elif mn == 5: 
            p = int (input ("Insira o calor com o qual quer comparar a precipitação: "))
            print (diasChuvosos (TabMeteo7, p))

        elif mn == 6:
            p = int (input ("Insira o valor com o qual quer comparar a precipitação: "))
            print (maxPeriodoCalor (TabMeteo7, p))

        elif mn == 7:
            print (grafTabMeteo (TabMeteo7))

        elif mn == 8:
            fnome = input ("Escolha o nome que quer dar ao ficheiro: ")
            guardaTabMeteo (TabMeteo7, fnome)
            print (f"Ficheiro {fnome} guardado com sucesso!")

        elif mn == 9:
           print( carregaTabMeteo (fnome))

        elif mn == 0:
            print ("Terminou de realizar operações. Até à próxima!")







menu ()
