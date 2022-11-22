#08/10/2022
#020 -O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
n1 = str(input("Primeiro aluno da lista: "))
n2 = str(input("Segundo aluno na lista: "))
n3 = str(input("Terceiro aluno na lista: "))
n4 = str(input("Quarto aluno na lista: "))
lista = [n1,n2,n3,n4]
shuffle(lista)
print("A oderm de apresentação será: \n{}".format(lista))

#DIFERENÇA DO CURSO EM VIDEO:
#n1 = str(input("Primeiro aluno: "))
#No final ele printa a lista gora do primeiro print;