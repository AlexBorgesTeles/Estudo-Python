#09/10/2022
#06- CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE OS EU DOBRO, TRIPLO E RAIZ QUADRADA.
#print("DESCUBRA O DOBRO, O TRIPLO E A RAIZ QUADRADA!!")
#numb = int(input("Digite um número: "))
#dobro = numb * 2
#triplo = numb * 3
#raiz = numb ** 2
#print("O número {} resulta: \nO dobro {} \nO triplo {} \nA raíz quadrada {}".format(numb,dobro,triplo,raiz))

#CORREÇÃO DO CURSO EM VIDEO:
#Erro de fórmula:
#n = int(input("Digite um número: "))
#d = n * 2
#t = n * 3
#r = n ** (1/2)
#print("O dobro de {} vale {}".format(n,d))
#print("O triplo de {} vale {}. \nA raíz quadrada de {} é igual a {:.2f}.".format(n, t, n, r))

#VERSÃO DE UMA VARIAVEL APENAS:
n = int(input("Digite um número: "))
print("O dobro de {} vale {}.".format(n, (n*2)))
print("O triplo de {} vale {}. \nA raíz quadrada de {} é igual {:.2f}".format(n, (n*3), n, (n**(1/2))))
#pow(n, (1/2)) - serve como raiz quadrada;