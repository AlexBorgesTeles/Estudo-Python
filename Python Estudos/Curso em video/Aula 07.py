#07/10/2022 https://www.youtube.com/watch?v=Vw6gLypRKmY&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=12
Nome = input("Qual é seu nome?")
print("Prazer em te conhecer {:=>20}!".format(Nome))
#{:20} – Vai escrever com espaço limitado de 20 caracteres;
#{:<20}-Escreva no início; {:>20}-Escreva no final; {:^20}-Escreva no centro;
#{:=20} {:=^20} {:=<20} {:=>20}- Print o máximo possível de = com acréscimo do formatado
n1 = int(input("Digite um valor: "))
n2 = int(input("Outro valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A soma é {},\n o produto é {}\n e a divisão é {:.3f}".format(s,m,d), end=" ")
#{:.3f} -> De limitar quantos digitos um número float
#,end=" " -> permite que a linha não se quebre e continue com a de baixo, mesmo sendo prints
#\n -> pode ser usado no meio das "" para quebrar
print("Divisão inteira {}\n e potência {}".format(di, e))

#05 – FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR.
#06- CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE OS EU DOBRO, TRIPLO E RAIZ QUADRADA.
#07- DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO,CALCULA E MOSTRE MÉDIA
#08-ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILÍMETROS.
#09-FAÇA EM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE NA TELA A SUA TABUADA.
#10-CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR. CONSIDERE US$1,00 = R$3,27
#11-FAÇA UM PROGRAMA QUE ELIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2M QUADRADO.
#12-FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO.
#13- FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO.

