# Escreva um programa em Python que leia a cotação do dólar (taxa de conversão), leia um valor em dólares e converta e mostre o valor equivalente em Reais.
dolar = float(input('Quantos dolar quer converter? '))
print('Cotação está sendo feita a R$5,31')
reais = 5.31 * dolar
print('{:.2f} Dolar são {:.2f} Reais.'.format(dolar,reais))