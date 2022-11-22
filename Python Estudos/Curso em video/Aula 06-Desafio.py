#Sexta Aula, com desfio (06/10/2022):
#https://www.youtube.com/watch?v=hdDHg1p3YVc&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=9
# 03. Crie um programa que leia dois números e mostre a soma entre eles.
print("SOMANDO VALORES")
n1=int(input("Digite um número a ser somado: "))
n2=int(input("Digite outro número a ser somado: "))
soma= n1+n2;
#print("A soma de",n1," + ",n2,", resulta em: {}".format(soma))
print("A soma de {} + {}, resulta em: {}".format(n1,n2,soma))

#Sexta Aula, com desfio (06/10/2022):
#https://www.youtube.com/watch?v=hdDHg1p3YVc&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=9
#04. Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.
print("ANALISADOR DE VALOR!!!")
n1 = input("Digite algo para ser lido pelo analisador:")
print("O seu tipo é:",type("{}").format(n1))
print("Ele é um valor númerico?",n1.isnumeric())
print("Ele é um valor alpha?",n1.isalpha())
print("Ele é um valor númerico e alpha?",n1.isalnum())
print("Ele é um valor com texto maiscul?a",n1.isupper())

