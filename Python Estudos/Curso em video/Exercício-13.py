#09/10/2022
#13- FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO.
salario = float(input("insira o seu salário atual: R$"))
aumento = salario * 1.15
print("Seu novo salario é de: \nRS{}".format(aumento))

#ESCRITA DO CURSO EM VIDEO
salário = float(input("Qual é o salário do Funcionário? R$"))
novo = salário + (salário * 15/100)
print("Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(salário, novo))