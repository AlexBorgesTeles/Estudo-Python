#17/11/2022
#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra “A”.
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.

#MINHA RESPSOTA PESSOAL: (21/12/2022 realizei apenas metade do código, tive que ver o video)
#frase = str(input("Digite uma frase: \n")).upper().strip()
#print("Sua frase possui {} de letras A.".format(frase.count("A")))
#print("Sendo a primeira letra encontrada na posição: {}".format(frase.find("A")+1))
#print("Sendo a última na posição: {}".format(frase.rfind("A")+1))

#RESPOSTA DO CURSO EM VIDEO: (21/11/202)
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1)) #<- O +1 é para indicar na posição lida pelo usuário e nãoda máquina que é do começo 0
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))