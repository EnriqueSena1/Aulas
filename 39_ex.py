# 39
'''gabarito=["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]
aluno=[]


while True:
    nome=input("Digite nome do aluno, ou X para sair: ")
    if nome=="X":
        break
    respostas=[]
    acertos=0

    for i in range (len(gabarito)):
        respostas.append(input(f"resposta da questão{i+1}(A,B,C,D,E):"))

        if respostas[i]==gabarito[i]:
            acertos+=1
    aluno.append([nome, respostas,acertos])

maior=["",0]
menor=["",10]
soma=0
for item in aluno:
    if item[2]> maior[1]:
        maior[1]= item [2]
        maior[0]= item[0]

    if item[2] < menor[1]:
        menor[1]= item [2]
        menor[0]= item [0]
    soma+=item[2]

print(f"{len(aluno)} alunos responderam, sendo a media de {soma/len(aluno)} pontos, a maior nota foi {maior[1]} de menor nota foi {maior[0]}, e a menor nota foi {menor[1]} de menor nota foi {menor[0]}")'''