#35
"""
valor_do_saque = int(input('Digite o valor do saque: R$'))
total = valor_do_saque

cedula = 100
total_de_cedulas = 0

while True:
    if valor_do_saque >= cedula:
        valor_do_saque -= cedula
        total_de_cedulas += 1
    else:
        if total_de_cedulas > 0:
            print(f"Total de {total_de_cedulas} cédulas de R${cedula}...[OK]")
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        total_de_cedulas = 0

    if valor_do_saque == 0:
        print('=' * 40)
        print(f"Transação realizada com sucesso!\nSaque no valor total de --> : R${total}")
        exit()
    elif valor_do_saque == 1:
        print("\nOPERAÇÃO CANCELADA!\nAs cédulas disponíveis neste caixa não permitem concluir esta transação."
              "\nPor favor, refaça sua operação com outro valor!")
        exit()


"""