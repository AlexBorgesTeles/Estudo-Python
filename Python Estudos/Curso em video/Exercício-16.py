#08/10/2022
#016 – Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex.Digite um número: 6.127 O número 6.127 tem a parte Inteira 6.
#from math import floor
#num = float(input("DIgite um número aqui: "))
#print("O valor inteiro de {}, é : {}".format(num,floor(num)))

#EXEMPLOS DO CURSO EM VIDEO:
#from math import trunc
#num = float(input("Digite um valor: "))
#print("O valor digitado foi {} e a sua porção inteira é {}".format(num, trunc(num)))

num = float(input("Digite um valor: "))
print("O valor digitado foi {} e a sua porção inteira e {}".format(num, int(num)))


