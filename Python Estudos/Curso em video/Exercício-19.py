#08/10/2022
#019 – Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
n1 = str(input("Digite o nome do priemiro aluno: "))
n2 = str(input("Digite o nome do segundo aluno: "))
n3 = str(input("Digite o nome do terceiro aluno: "))
n4 = str(input("Digite o nome do quarto aluno: "))
lista = [n1,n2,n3,n4]
escolha = choice(lista)
print("O aluno é escolhio é {}".format(escolha))

#DIFERENÇA DO CUSRO EM VIDEO:
#n1 = str(input("Primeiro aluno:")) ... os outros também seguem uma escrita diferente;
#print("O alunoescolhido fooi {}".format(escolhido))