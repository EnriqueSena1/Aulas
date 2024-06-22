#38
"""
# regra 1 
a = int(input("Digite o primeiro número (a): "))
b = int(input("Digite o segundo número (b): "))

sequencia = [a, b]

# regra 5
while a + b != 1:
    # regra 2
    soma = a + b
    # regra 3
    if soma % 2 == 1:
        # regra 3
        sequencia.append(soma)
        a, b = b, soma
    else:
        # regra 4
        sequencia.append(soma // 2)
        a, b = b, soma // 2

# regra 6
print(f"Sequência gerada ", [sequencia])

"""