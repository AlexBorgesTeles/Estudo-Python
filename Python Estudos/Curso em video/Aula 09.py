#17/11/2022
#MANIPULANDO TEXTO
frase = 'Curso em Vídeo Python'
#Contando do primeiro até o 15, pulando 2 em 2;
print(frase[1:15:2])
#Contnado tudo, apenas 2 em 2;
print(frase[::2])
#Printar textos longos usas se """;
print("""A grande conquista humana foi o descobrimento do fogo.
Afinal com essa ferramenta, a produção de comida e proteção do
meio selvagem foi muitas vezes melhorado.""")
#Toda string é considerado um objeto;
print(frase.count('o'))
#Podemos unir conceitos como .upper e .count. nesse caso vamos mudar a string e contar os resultados mudados específicos;
print(frase.upper().count("O"))
#Também com len()
print(len(frase))
#Retirado o espaço na contagem
print(len(frase.strip()))
#Replace para sua substituição nessa instância;
print(frase.replace('Python','Android'))
print(frase)
#Para realizar a substituição efitivamente:
frase = frase.replace('Python','Android')
print(frase)
#Exemplo com in ,ou seja, ver se um valor está dentro da string (True/false):
print('Curso' in frase)
#Para realizar uma contagem de onde na string ele existe é o .find():
print(frase.find('Curso'))
print(frase.lower().find('vídeo'))
#Para dividir cada palavras separada em espaço como uma string diferente usa .split():
dividido = frase.split()
print(dividido[2]) # <- Pegue o dividido e pegue da lista feita os egundo objeto;
print(dividido[2][3]) # <- Semelahnte do acima, mais ele no final vai procurar o quarto caractere do obejto chamado;