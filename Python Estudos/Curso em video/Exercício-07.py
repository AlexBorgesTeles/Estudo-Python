#09/10/2022
#07- DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO,CALCULA E MOSTRE MÉDIA
print("MÉDIA ESCOLAR!!!")
nome = input("Nome do Aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
#media = nota1 + nota2 / 2 -- Houve um erro e foi corrigido no video;
media = (nota1 + nota2) / 2
#print("A ficha escolar de {} \nA primeira nota {} \nA segunda nota {}\nA media é {}".format(nome,nota1,nota2,media))
print("A ficha escolar de {} \nA primeira nota é {} \nA segunda nota é {} \nA média é {:.1f}".format(nome,nota1,nota2,media))
#O uso do {:.1f} para reduzir a quantidade de casas decimais a serem visiveis, ou seja, "Depois do ponto flutuante coloque 1 dígito.
#Causando a regra de arrondamento no seu uso