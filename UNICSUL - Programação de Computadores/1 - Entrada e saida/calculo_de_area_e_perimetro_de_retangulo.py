# Desenvolva um programa em Python que solicite ao usuário os valores dos lados de um retângulo e calcule e mostre seu perímetro e sua área.
num1 = float(input('Qual altura do retangulo? '))
num2 = float(input('Qual largura do retangulo? '))
perimetro = 2 * (num1+num2)
area = num1 * num2
print('Area: {} e o Perimetro: {} do seu retangulo.'.format(area,perimetro))