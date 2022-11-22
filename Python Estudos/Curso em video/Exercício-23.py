#17/11/2022
#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

#RESPOSTA PESSOAL
#nume = str(input("Digite um valor de 0 a 9999: ")).split()
#print(" Unidade: ",nume[3],"\n Dezena:",nume[2],"\n Centena: ",nume[1],"\n Milhar: ",nume[0])

#RESPOSTA DO CURSO EM VIDEO: (21/12/2022)
num = int(input('Informe um número: '))
u = num // 1% 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}.'.format(num))
print('unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))