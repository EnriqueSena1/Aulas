# 40

'''livros=[["Comer, rezar e amar", "Elizabeht gilbert", "Disponivel"], ["Mil dias na Toscana", "Madalena de Blasi", "Disponivel"], ["50 tons de cinza", "E.L Jmaes", "Disponivel"]]

while True:
    usuario=input("Digite seu primeiro Nome: ")
    print(f'Olá, {usuario}')
    print("Opções da Biblioteca")
    print("Opção 1: Adicionar Livros")
    print("Opção 2: Livros Disponiveis")
    print("Opção 3: Emprestar Livros")
    print("Opção 4: Devolver Livros")
    print("Opção -1: Sair")
    
    o=int(input("Digite uma opção acima: "))
    
    if o==1:
        print("Adicione o Livro ")
        livros.append([input("Digite nome do livro: "), input("Digite Autor: "), "Disponivel"])

    elif o==2:
        for indice in range(len(livros)):
            if livros[indice][2]== "Disponivel":
                print(f"ID {indice} - {livros[indice][0]}: {livros[indice][1]}")
        
    elif o==3:
        print("Emprestar Livros")
        id=int(input("Informe o ID do livro desejado: "))
        if livros[id][2]=="Disponivel":
            livros[id][2]="Indisponivel" 
            print (f"O {livros[id][0]} emprestado com sucesso!")
        else:
            print("Livro Indisponivel")
        

    elif o==4:
        print("Devolver Livros")

        id=int(input("Informe o ID do livro que deseja devolver: "))
        if livros[id][2]=="Indisponivel":
            livros[id][2]="Disponivel" 
            print (f"O {livros[id][0]} foi devolvido com sucesso!")
        else:
            print("Livro não esta emprestado")


    elif o==-1:
        print("Sair")
        break
'''