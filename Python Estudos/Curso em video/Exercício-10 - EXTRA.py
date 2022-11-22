#24/10/2022
#10-CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES E EUROS ELA PODE COMPRAR.
real = float(input("Quanto de dinheiro você tem na carteira: R$"))
dollar = real / 5.303
euro = real / 5.236
print("Você tem R$ {:.2f} , consegue comprar de: \nDOLLAR: {:.2f} \nEURO: {:.2f} ".format(real,dollar,euro))
