# Faça um programa em Python que obtenha o valor de uma compra, calcular e mostrar o valor da compra considerando o desconto, conforme descrito abaixo:
# Para compras acima de R$ 200 a loja dá um desconto de 20% Para as abaixo disso não tem desconto, mostre o valor da compra.
compra = float(input('Qual o valor total da compra? '))
if compra >= 200.00:
  desconto = compra * 0.20
  print(f'Total da compra: {compra-desconto} Desconto de {desconto}.')
else:
  print(f'Total da compra: {compra}.')