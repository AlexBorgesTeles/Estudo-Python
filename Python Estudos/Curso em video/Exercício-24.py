#17/11/2022
#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

#RESPOSTA PESSOAL
#nome = str(input("Digite o nome de uma cidade: "))
#filtro = (nome.strip().upper()[0:5])
#print("Existe Santo nesse nome: ", "SANTO" in filtro )

#RESPOSTA DO CURSO EM VIDEO: (21/12/2022)
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')