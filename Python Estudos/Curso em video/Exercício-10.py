#09/10/2022
#10-CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR.
# CONSIDERE US$1,00 = R$3,27
print("CONVERSÃOD E REAIS PARA DÓLARES!!")
#money = float(input("Insira um valor em reais desejado: R$")) -- Não tem sentido com a pergunta;
money = float(input("Quanto de dinhero você tem na carteira ? R$"))
#conv = money * 3.27 - Erro de fórmula
conv = money / 3.27
print("Convertendo R${} em doláres fica:\nUS${:.1f}".format(money,conv))
