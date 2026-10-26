# Crie um programa em Python que solicite ao usuário a sua idade expressa em anos, meses e dias (variáveis separadas). 
# Calcule e mostre a idade expressa apenas em dias. Para isso considere 1 ano = 365 dias, 1 mês = 30 dias.
idade=int(input('Digite a idade:'))
mes=int(input('Digite o mês:'))
dia=int(input('Digite o dia:'))
imd=idade*365+mes*30+dia
print(imd)