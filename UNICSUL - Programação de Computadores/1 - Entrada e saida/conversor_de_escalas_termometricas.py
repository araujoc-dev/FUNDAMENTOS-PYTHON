# Escreva um programa em Python que obtenha uma temperatura em graus Celsius, calcule e mostre a respectiva temperatura nas escalas Fahrenheit e Kelvin.
C = float(input('Qual a temperatura em Celcius? '))
F = (C * 1.8) + 32
K = C + 273.1
print('{}º Celcius Em fahrenheit é {} e em Kelvin é {}'.format(C,F,K))