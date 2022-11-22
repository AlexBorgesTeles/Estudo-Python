#07/10/2022 https://www.youtube.com/watch?v=tHYxjJxtJko&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=11
#04. Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
a = input("Digite algo: ")
print("O tipo primitivo desse valor é ",type(a))
print("Só tem espaços? ",a.isspace())
print("É um número? ",a.isnumeric())
print("É alfabético? ",a.isalpha())
print("É alfanumérico? ",a.isalnum())
print("Está em maiúsculas? ",a.isupper())
print("Está em minúsculas? ",a.islower())
print("Está capitalizada? ",a.istitle())
