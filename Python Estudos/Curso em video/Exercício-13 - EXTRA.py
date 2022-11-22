#09/10/2022
#13- EXTRA - Realize uma conta sobre um produto se for avista (com 10% desconto), ou parcelado ( 8% de aumento do juros);
produto = float(input("AVISTA 10% DE DESCONTO! PARCELADO 8% DE JUROS! \nQuanto é o valor do produto que deseja comprar ? R$"))
avista = produto - (produto * 10/100)
parcela = produto + (produto * 8/100)
print(" O produto vale R${:.2f}, assim se pagar avista fica R${:.2f};"
      "\n Parcelado em 2x R${:.2f};"
      "\n Parcelado em 3x R${:.2f};"
      "\n Parcelado em 4x R${:.2f};"
      "\n Parcelado em 5x R${:.2f};".format(produto,avista,parcela,parcela+(produto*8/100),parcela+(2*produto*8/100),parcela+(3*produto*8/100),parcela+(4*produto*8/100)))
