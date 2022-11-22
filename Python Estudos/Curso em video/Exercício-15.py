#27/10/2022
#15-Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
#km = float(input("Quantos km o carro percorreu ? Km: "))
#dia = int(input("Quantos dias ele foi alugado ? Dias: "))
#custo = (60 * dia) + (0.15 * km)
#print("O carro alugado percorreu {}Km e foi alugado a {} dias. O Custo total dá R${:.2f}".format(km,dia,custo))

#ESCRITA DO CURSO EM VIDEO
dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
pago = (dias * 60) + (km * 0.15)
print("O total a pagar é de R${:.2f}".format(pago))
