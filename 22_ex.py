# 22
'''
numero = int(input("Didite um valor para verificar se numero e um Triangulo: "))
y = 1
x = 2
z = 3
controle = True # e importante colocar um (controlador = True )se não fica em loop infinitos
produto = y * x * z 

while produto <= numero and controle:  
    if produto == numero:
        controle = False # estou definindo que quando for falso ele tem que ir para o "if"
    y+=1
    x+=1
    z+=1
    produto = y * x * z 

if controle == False:
    print(f"Numero e um triangulo{numero}")
else:
    print(f"Numero não e um Triangulo {numero}")'''
