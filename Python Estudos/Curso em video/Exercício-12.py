#09/10/2022
#12-FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO.
#preco = float(input("Digite o preço do produto a ser descontado: R$"))
#desconto = preco -(preco * 0.05)
#print("O desconto do produto é de: R${}".format(desconto))

#PROGRAMAÇÃO DO VIDEO EM CURSO
preço = float(input("Qual é o preço do produto? R$"))
novo = preço - (preço*5 /100)
print("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}".format(preço, novo))