#08/10/2022
#018-Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
#from math import radians,cos,sin,tan
#angulo = float(input("Digite um ângulo qualquer: "))
#rad = radians(angulo)
#print("O seu ângulo {} tem:\nO Cosseno {:.2f}\nO Seno {:.2f}\nA Tangente {:.2f}".format(angulo,cos(rad),sin(rad),tan(rad)))

#VERSÃO DO CURSO EM VIDEO:
from math import radians, sin, cos, tan
ângulo = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(ângulo))
print("O ãngulo de {} tem o SENO de {:.2f}".format(ângulo, seno))
cosseno = cos(radians(ângulo))
print("O ãngulo de {} tem o Cosseno de {:.2f}".format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(ângulo, tangente))