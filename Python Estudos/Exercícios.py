#Primeira aula de exercicio(01/08/2022):
# https://www.youtube.com/watch?v=nIHq1MtJaKs&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=7
#Desafio 01 - Crie um programa que escreva"Olá, mundo!" na tela.
print("Olá,Mundo!") #Uso de print!

#Segunda aula de exercicio(01/08/2022):
# https://www.youtube.com/watch?v=FNqdV5Zb_5Q&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=8
#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
resposta = input("Qual é o seu nome ? \n")#Uso de uma variavel
print("Boas-vindas ",resposta,"!")
print("é um prazer te conhecer, {}".format(resposta))

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
print("Ele é um valor com texto maiscula?",n1.isupper())

#09/10/2022
#05 – FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR.
print("DESCUBRA OS NÚMEROS ANTECESSORES E SUCESSORES!!")
inteiro = int(input("Digite um número: "))
antecessor = inteiro - 1
sucessor = inteiro + 1
print("O número {}: \nSeu sucessor {} \nSeu antecessor {}!".format(inteiro,sucessor,antecessor))

#09/10/2022
#06- CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE OS EU DOBRO, TRIPLO E RAIZ QUADRADA.
print("DESCUBRA O DOBRO, O TRIPLO E A RAIZ QUADRADA!!")
numb = int(input("Digite um número: "))
dobro = numb * 2
triplo = numb * 3
raiz = numb ** (1/2)#CORRIGIDO11/10/2022
print("O número {} resulta: \nO dobro {} \nO triplo {} \nA raíz quadrada {}".format(numb,dobro,triplo,raiz))

#09/10/2022
#07- DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO,CALCULA E MOSTRE MÉDIA
print("MÉDIA ESCOLAR!!!")
nome = input("Nome do Aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = nota1 + nota2 / 2
print("A ficha escolar de {} \nA primeira nota {} \nA segunda nota {}\nA media é {}".format(nome,nota1,nota2,media))

#09/10/2022
#08-ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILÍMETROS.
print("TRANSFORMADOR DE METROS PARA CENTIMETROS E MILIMETROS!!")
m = float(input("Digite o valor em metros: "))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print("QUILÔMETRO: {:}km "
      "\nHECTÔMETRO: {}hm "
      "\nDECÂMETRO: {}dam "
      "\nMETRO: {:.0f}m "
      "\nDECÍMETRO: {}dm "
      "\nCENTÍMETRO: {}cm "
      "\nMILÍMETRO: {}mm".format(km,hm,dam,m,dm,cm,mm))

#09/10/2022
#09-FAÇA EM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE NA TELA A SUA TABUADA.
numb = int(input("Digite um número para ver a sua tabuada:"))
print("-"*15)
print("{} x {:2} = {}".format(numb,1,numb*1)) #{:2} Esse terá dois dígitos;
print("{} x {:2} = {}".format(numb,2,numb*2))
print("{} x {:2} = {}".format(numb,3,numb*3))
print("{} x {:2} = {}".format(numb,4,numb*4))
print("{} x {:2} = {}".format(numb,5,numb*5))
print("{} x {:2} = {}".format(numb,6,numb*6))
print("{} x {:2} = {}".format(numb,7,numb*7))
print("{} x {:2} = {}".format(numb,8,numb*8))
print("{} x {:2} = {}".format(numb,9,numb*9))
print("{} x {:2} = {}".format(numb,10,numb*10))
print("-"*15)

#09/10/2022
#11-FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA
#NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2M QUADRADO.
larg = float(input("Largura de parede: "))
alt = float(input("Altura da parede: "))
área = larg * alt
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m2.".format(larg, alt, área))
tinta = área / 2
print("Para pintar essa parede, você precisará de {}l de tinta.".format(tinta))

#09/10/2022
#12-FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO.
preço = float(input("Qual é o preço do produto? R$"))
novo = preço - (preço*5 /100)
print("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}".format(preço, novo))

#09/10/2022
#13- FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO.
salário = float(input("Qual é o salário do Funcionário? R$"))
novo = salário + (salário * 15/100)
print("Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(salário, novo))

#27/10/2022
#14-Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input("Informe a temperatura em C: "))
f = 9*c/5 + 32
print("A temperatura de {1}C corresponde a {0}F". format(f,c))