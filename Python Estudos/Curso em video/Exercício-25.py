#17/11/2022
#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

#RESPOSTA PESSOAL
#nome = str(input("Digite um nome: "))
#filtro = nome.upper().split()
#print("O nome digitado possui Silva: ", "SILVA" in filtro)

#RESPOSTA DO VIDEO EM CURSO: (21/11/2022)
nome = str(input('Qual é o seu nome completo? '))
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))