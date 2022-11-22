#09/10/2022
#11-FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA
#NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2M QUADRADO.
#altura = float(input("Digite a altura da parede: "))
#largura = float(input("Digite a largura da parede: "))
#area_t = altura * largura
#litro = area_t /2

#print("A área da parede ao total é: {}m quadrados \nE gasta {} litros de tinta".format(area_t,litro))

#PROGRAMAÇÃO DO CURSO EM VIDEO
larg = float(input("Largura de parede: "))
alt = float(input("Altura da parede: "))
área = larg * alt
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m2.".format(larg, alt, área))
tinta = área / 2
print("Para pintar essa parede, você precisará de {}l de tinta.".format(tinta))