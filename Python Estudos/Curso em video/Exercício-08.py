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