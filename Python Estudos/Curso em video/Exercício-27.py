#17/11/2022
#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

#RESPOSTA PESSOAL:
#nome = str(input("Digite um nome: "))
#filtro = nome.strip().split()
#print("Primeiro nome: ",filtro[0])
#print("Último nome: ",filtro[-1])

#RESPOSTA DO VIDEO EM CURSO: (21/12/2022)
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1])) #<- Ele sempre vai contar o total e vai voltar uma casa iniciando, forçando que leia a última.