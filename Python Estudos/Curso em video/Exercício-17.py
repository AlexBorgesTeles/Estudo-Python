#08/10/2022
#17-Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa. EXEMPLO: CO=3 e CA=4, tem que dar 5.
#from math import hypot
#co = float(input("Digite o cateto oposto: "))
#ca = float(input("Digite o cateto adjacente: "))
#print("O triângulo com C.Oposto {} e C.Ajacente {}, tem a hipotenusa de {:.2f}.".format(co,ca,hypot(co,ca)))

#VERSÃO DO CURSO EM VIDEO:
#co = float(input("O comprimento do cateto oposto: "))
#ca = float(input("O comprimento do cateto adjacente: "))
#hi = (co**2+ca**2)**(1/2)
#print("A hipotenusa vai medir {:.2f}".format(hi))

from math import hypot
co = float(input("Comprimento de cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = hypot(co, ca)
print("A hipotenusa vai medir {:.2f}".format(hi))