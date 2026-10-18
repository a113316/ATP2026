def Criarturma ():
    turma = []
    nometurma = input ("Turma criada. Quer dar um nome? ")
    print (f"Criou a turma: {nometurma}")
    return []

def ExisteId (id, turma):
    existe = False
    for aluno in turma:
        if aluno [1] == id:
            existe = True 
    return existe

def InserirAluno (turma):
    
    nome = input ("Insira o nome d@ alun@: ")
    id = input("Insira o id d@ alun@: ")
    while ExisteId (id, turma):
       id = input ("Já existe um aluno com esse Id. Escolha outro: ")
    notaTPC = LerNota ("Insira a nota do TPC d@ alun@: ")
    notaProj = LerNota ("Insira a nota do projeto d@ alun@: ")
    notaTeste = LerNota ("Insira a nota do teste d@ aluno@: ")
    aluno = (nome, id, [notaTPC, notaProj, notaTeste])
    turma.append (aluno)
    print ("Novo aluno na turma :)")

def LerNota (texto):
    nota = float(input("Introduza uma nota de 0 a 20: "))
    while nota < 0 or nota > 20:
        nota = float(input("Valor Inválido. Introduza uma nota de 0 a 20: "))
    return nota 

def Listarturma (turma):
    for aluno in turma:
        print (f"Nome - {aluno[0]}\nId - {aluno[1]}\nNota do Tpc - {aluno[2][0]}\nNota do Projeto - {aluno[2][1]}\nNota do Teste - {aluno[2][2]}\n")

def ConsultarId (id, turma):
    id = input("Insira o id que deseja procurar: ")
    encontrado = False 
    for aluno in turma:
        if aluno [1] == id:
            print (f"Aqui estão as informações do aluno que procura:\nNome - {aluno[0]}\nId - {aluno[1]}\nNota do Tpc - {aluno[2][0]}\nNota do Projeto - {aluno[2][1]}\nNota do Teste - {aluno[2][2]}\n")
            encontrado = True 
    if not encontrado: 
        print ("O aluno em questão não está nesta turma. ")
    return encontrado 
        
def GuardarTurma (turma):
    nomeFicheiro = input("Escolha o nome do ficheiro: ")
    file = open(nomeFicheiro,"w") 
    for aluno in turma:
            nome, id, notas = aluno
            file.write(f"{nome}@{id}@{notas[0]}@{notas[1]}@{notas[2]}\n")
    file.close()
    print (f"{len(turma)} alunos guardados em {nomeFicheiro} ")
    

def CarregarTurma (nomeFicheiro):
    turma = []
    file = open(nomeFicheiro,"r")
    for line in file:
        informacao = line.split ("@")
        nome = informacao [0]
        id = informacao [1]
        notas = [float(informacao [2]),float (informacao [3]), float (informacao[4])]
        aluno = (nome, id, notas) 
        turma.append (aluno)

    file.close()
    return turma


def menu ():
    turma = []
    mn = -1
    while mn != 0:
        print ("""
    Qual a operação que deseja fazer?
    1 - Criar uma turma;
    2 - Inserir um aluno na turma;
    3 - Listar a turma;
    4 - Consultar um aluno por id; 
    5 - Guardar a turma em ficheiro;
    6 - Carregar uma turma de um ficheiro;
    0 - Sair da aplicação.  """)

        mn = int (input("Escolha um número de 0 a 6: "))
        if mn == 1:
            Criarturma ()
        elif mn == 2:
            InserirAluno (turma)
        elif mn == 3:
            Listarturma (turma)
        elif mn == 4:
            ConsultarId (id,turma)
        elif mn == 5: 
            GuardarTurma (turma)
        elif mn == 6:
           nomeFicheiro = input ("Escolha o nome do ficheiro que quer carregar: ")
           turma = CarregarTurma (nomeFicheiro)
           print (turma)
        elif mn == 0:
            print ("Terminou de realizar operações. Até à próxima!")

menu ()