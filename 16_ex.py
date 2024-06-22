# 16 loja de tintas
"""
metragem=float(input("qtd de metros quadrados: "))

rendimento=6

lata=18

valorLata=80.00

galao=3.6

valorGalao=25.00

litros=(metragem/rendimento)
print("Litros ",litros)

litros+=litros*0.10

litros=17
print("Litros ",litros)

qtdLata=litros//lata

restoLata=litros%lata

qtdLataGalao=qtdLata

restoToGalao=0

if restoLata>0:
    qtdLata+=1
    restoToGalao=18*(restoLata/100)
    
valorTotalLata=qtdLata*valorLata
print("Você pode comprar  "+str(qtdLata)+" Lata(s) no valor total de R$ "+str(valorTotalLata))
print("Ou")

qtdGalao=litros//galao
restoGalao=litros%galao
if restoGalao>0:
    qtdGalao+=1

valorTotalGalao=qtdGalao*valorGalao
print("Comprar "+str(qtdGalao)+" Galão(oes) no valor total de R$ "+str(valorTotalGalao))
print("Ou")
if litros>=lata:
    print("Modelo misto, "+str(qtdLataGalao)+" Lata(s) ")
    valorTotalGalao=0
else:
    print("Modelo misto, 0 Lata(s) ")
    restoToGalao=litros

if restoToGalao>0:
    qtdGalao=restoToGalao//galao
    restoGalao=restoToGalao%galao
    if restoGalao>0:
        qtdGalao+=1
    print("E "+str(qtdGalao)+" Galao(oes) ")
    valorTotalGalao=qtdGalao*valorGalao
valorTotal=(qtdLataGalao*valorLata)+valorTotalGalao
print("Valor Total R$ "+str(valorTotal)+"")
"""