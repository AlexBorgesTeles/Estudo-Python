#17/11/2022
#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas;
#O nome com todas minúsculas;
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.
#Desafio(023):

#RESPOSTA PESSOAL: (Corrigida pois estava completamente errada os dois últimos prints))
#nome = str(input("Digite um nome: "))
#print("Letras maiúsculas: {}.".format(nome.upper().strip()))
#print("Letras minúsculas: {}.".format(nome.lower().strip()))
#print("Quantas letras nome completo: {}.".format(len(nome) - nome.count(' ')))
#divide = nome.split()
#print("Quantas letras letras no primeiro nome: {}.".format(len(divide[0])))

#RESPOSTA DO VIDEO EM CURSO: (21/12/2022)
nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
print("Seu nome em maiùscula é {}.".format(nome.upper()))
print("Seu nome em  minùscula é {}.".format(nome.lower()))
print("Seu nome tem ao todo {} letras.".format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras.".format(separa[0], len(separa[0])))