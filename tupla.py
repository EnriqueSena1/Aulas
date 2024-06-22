# Questão 01
'''tupla = (1, 2, 3,0,4, 5, 6)
zero_entrado = False

for i in tupla:
    if i == 0:
        print("Encontrado Zero")
        zero_entrado = True
        break

if not zero_entrado:
    print("Não foi encontrado Zero")'''
# Questão 02

'''tupla = (3, 6, 2, 9, 1, 7, 5)
maior_numero = tupla[0] 

for numero in tupla:
    if numero > maior_numero:
        maior_numero = numero

print(f"O maior número na tupla é: {maior_numero}")'''
# Questão 03

'''tupla = (1, 2, 3, 4, 5, 6)
for i in tupla:
    if i % 2 == 0:
        print(i)'''
# Questão 04 
"""
tupla = (1, 2, 3, 4, 5, 6, 7, 8)
total = 0

for numero in tupla:
    if numero % 2 == 0:
        total += numero

print(f"A soma dos números pares é:{total}", )
"""

# Questão 05
"""
tupla = (3, 8, 2, 10, 6, 4)
for num in tupla:
    if num > 5:
        print(num)
"""

# Questão 06
"""
alunos = [("João", 8.0), ("Maria", 9.5), ("Pedro", 7.5), ("Ana", 8.5)]

maior_nota = float("-inf")

for nome, nota in alunos:
    if nota > maior_nota:
        maior_nota = nota
        aluno_com_maior_nota = nome

print(f"A maior nota é {aluno_com_maior_nota} com nota {maior_nota}.")
"""

# Questão 07
"""
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

soma = 0

for i in matriz:
    for elemento in i:
        soma += elemento

print(f"A soma dos valores da matriz é: {soma}")
"""

# Questão 08
"""
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

T = [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

for i in T:
    print(i)
"""

# Questão 09
"""
matriz = [[1, 2, 11, 13], [4, 15, 16, 60], [7, 8, 19, 200], [20, 100, 5, 3]]

contador = 0
for i in matriz:
    for valor in i:
        if valor > 10:
            contador += 1

print(f"A matriz possui {contador} valores maiores que 10.")
"""

# Questão 10
"""
matriz = [[0] * 5 for _ in range(5)]

for i in range(5):
    matriz[i][i] = 1

for na_matriz in matriz:
    print(na_matriz)
"""

# Questão 11
"""
matriz = [[1, 2, 11, 13], [4, 15, 16, 60], [7, 8, 19, 200], [20, 100, 5, 3]]

maior_valor = matriz[0][0]
linha_maior_valor = 0
coluna_maior_valor = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]
            linha_maior_valor = i
            coluna_maior_valor = j

for linha in matriz:
    print(linha)

print(f"O maior valor ({maior_valor}) está na linha {linha_maior_valor + 1} e coluna {coluna_maior_valor + 1}.")
"""

#Questão 12
"""
M = [[1, 120, -3], [4, 5, 250], [7, 0, 9]]

maior_valor = M[0][0]
linha_maior_valor = 0
coluna_maior_valor = 0

menor_valor = M[0][0]
linha_menor_valor = 0
coluna_menor_valor = 0

for i in range(len(M)):
    for j in range(len(M[i])):
        if M[i][j] > maior_valor:
            maior_valor = M[i][j]
            linha_maior_valor = i
            coluna_maior_valor = j
        elif M[i][j] < menor_valor:
            menor_valor = M[i][j]
            linha_menor_valor = i
            coluna_menor_valor = j

for linha in M:
    print(linha)

print(f"O maior valor ({maior_valor}) está na linha {linha_maior_valor + 1} e coluna {coluna_maior_valor + 1}.")
print(f"O menor valor ({menor_valor}) está na linha {linha_menor_valor + 1} e coluna {coluna_menor_valor + 1}.")
"""

# Questão 13
"""
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

soma_diagonal_principal = 0

for i in range(len(matriz)):
    soma_diagonal_principal += matriz[i][i]

for linha in matriz:
    print(linha)

print(f"A soma dos elementos da diagonal principal é {soma_diagonal_principal}.")
"""

#Questão 14
"""
A = [[1, 13, 3], [4, 45, 67], [7, 80, 9]]
B = [[100, 8, 7], [6, 5, 4], [3, 25, 10]]

soma = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        soma[i][j] = A[i][j] + B[i][j]

for linha in soma:
    print(A)
    print(B)
    print(linha)
"""