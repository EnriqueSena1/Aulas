'''numero = int(input("Digite um número para a tabuada: "))

for i in range(1, 11):

    resultado = numero * i

    print(f"{numero} x {i} = {resultado}")



'''

'''dicio = {'num_passg': int(input("Digite numero da passagem: ")), "nome" : input("Digite o nome: "), "data": input("Digite a data: "), 'origem': input("Digite a Origem da viagem: "), 'destiino': input("Digite o destino: ")}
for x in dicio:
    print(f'{x} : {dicio[x]}')'''

'''dicionario = {"num":input("Digite numero da conta: "), "saldo":input("Digite o saldo da conta: "), "nome": input("Digite o nome do caboco: ")}
print(dicionario)'''

# lista de funcionario usando lista e dicionario

'''lista_funcionario = []
for i in range(4):
    funcionario = {}
    funcionario ["nome"] = input ("Digite o nome do caboco: ")
    funcionario ["funcont"] = input ("Digite a  função do caboco: ")
    funcionario ["salario"] = input ("Digite o salario do caboco: ")
    lista_funcionario.append (funcionario)

maior_salario = lista_funcionario[0]
for i in range(4):
    if lista_funcionario [i] ["salario"] > maior_salario ["salario"]:
        maior_salario = lista_funcionario[i]
print(maior_salario)'''








#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

while True:
        print("1. Adicionar Produto")
        print("2. Atualizar Estoque")
        print("3. Consultar Estoque")
        print("4. Listar Produtos")
        print("5. Sair")
        
        sla = int(input("Escolha uma opção acima"))

        if adicionar == 1:
            prod = {}
            prod ['produto']= input ("Digite o nome do produto:   ")
            prod ['quantidade']= int (input("Digite a quantidade inicial:   "))
            lista_estoque.append(prod)
                  
        elif remover == 2:
            aa = input("deseja remover ou adicionar ? ")
            if aa == 'adicionar':
                nome_produto = input("Digite o nome do produto: ")
                for i in lista_estoque:
                    if i['produto'] == nome_produto:
                        i ['quantidade']= int(input("digite a nova quantidade"))
            else:
                nome_produto = input("Digite o nome do produto: ")
                for i in lista_estoque:
                    if i['produto'] == nome_produto:
                        saida = int(input("digite a nova quantidade"))
                        i ['quantidade'] = i ['quantidade'] - saida

        elif sla == 3:
            nome_produto = input("digite o nome do produto")
            for i in lista_estoque:
                        if i ['produto'] == nome_produto:
                             print(i['quantidade'])
                        
        elif sla == 4:
            print(lista_estoque)
        else:
            break






 
# Estrutura de Dados:
# •	Cada turma deve conter as seguintes informações:
# •	Nome da Turma: Identificador exclusivo da turma.
# •	Lista de Alunos: Cada aluno deve ter um nome e uma lista de notas associadas.

turmas = {}

while True:
    print("1. Cadastrar Turma")
    print("2. Cadastrar Aluno")
    print("3. Atualizar Aluno")
    print("4. Remover Aluno")
    print("5. Visualizar Informações")
    op = input("Escolha uma opção: ")


# Requisitos do Sistema:
# •	Cadastrar Turmas:
# •	O sistema deve permitir que novas turmas sejam adicionadas.
# •	Cada turma deve ter um nome exclusivo.


    if op == 1:
        nome_turma = input("Digite o nome da turma: ")
        turmas[nome_turma] = []


# •	Cadastrar Alunos:
# •	O sistema deve permitir que alunos sejam adicionados a uma turma específica.
# •	Ao cadastrar um aluno, devem ser informados seu nome e suas notas.
# •	As notas devem ser inseridas como uma lista de valores numéricos.


    elif op == 2:
        nome_turma = input("Digite o nome da turma: ")
        if nome_turma in turmas:
            nome_aluno = input("Digite o nome do aluno: ")
            notas = input("Digite as notas do aluno: ")
            notas = [float(nota) for nota in notas.split(",")]
            turmas[nome_turma].append({"nome": nome_aluno, "notas": notas})
        else:
            print("Turma não encontrada!")

            
# •	Atualizar Informações de Alunos:
# •	O sistema deve permitir a atualização das informações de um aluno existente.
# •	Deve ser possível alterar o nome do aluno e/ou suas notas.


    elif op == 3:
        nome_turma = input("Digite o nome da turma: ")
        nome_aluno = input("Digite o nome do aluno: ")
        if nome_turma in turmas:
            for aluno in turmas[nome_turma]:
                if aluno["nome"] == nome_aluno:
                    notas = input("Digite as novas notas do aluno: ")
                    notas = [float(nota) for nota in notas.split(",")]
                    aluno["notas"] = notas
                    break
            else:
                print("Aluno não encontrado!")
        else:
            print("Turma não encontrada!")


# •	Remover Alunos:
# •	O sistema deve permitir que um aluno seja removido de uma turma específica.


    elif op == 4:
        nome_turma = input("Digite o nome da turma: ")
        nome_aluno = input("Digite o nome do aluno: ")
        if nome_turma in turmas:
            for aluno in turmas[nome_turma]:
                if aluno["nome"] == nome_aluno:
                    turmas[nome_turma].remove(aluno)
                    break
            else:
                print("Aluno não encontrado!")
        else:
            print("Turma não encontrada!")

# •	Visualizar Informações:
# •	O sistema deve permitir a visualização de todas as turmas cadastradas.
# •	Para cada turma, deve ser possível visualizar a lista de alunos e suas respectivas notas.


    elif op == 5:
        for turma, alunos in turmas.items():
            print(f"Turma: {turma}")
            for aluno in alunos:
                print(f"Aluno: {aluno['nome']}, Notas: {aluno['notas']}")
        break
    else:
        print("Opção inválida! Tente novamente.")
























"""
    dicio['Produto'] = input("Digite o nome do produto, e a quantidade inicial:  ")
    if dicio == :
        dicio['atualizar estoque' ]= input("Digite o nome do produto sugerido e a atualização da quantidade do produto sugerido:  ")
        dicio['Consultar Produto' ]= input("Qual nome do produto que deseja consultar:  ")

dicio['Listar Produtos' ]= input("Digite 'listar produtos' para listar todos os produtos e suas quantidades disponiveis  ")

for chave,valor in dicio.items():
    print(f'chave:"{chave}"- valor: "{valor}"')

            nome_produto = input("Digite o nome do produto: ")
        quantidade_inicial = int(input("Digite a quantidade inicial: "))
        estoque[nome_produto] = quantidade_inicial
        print(f"{nome_produto} adicionado ao estoque.")

    
    """