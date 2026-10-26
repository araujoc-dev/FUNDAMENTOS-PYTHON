# Escreva um programa em Python que calcule as duas raízes de uma equação de 2º grau ax²+bx+c, 
# conhecendo os valores dos coeficientes da mesma (a, b, c). Suponha que as raízes são reais. 
# Lembre-se que para calcular as duas raízes: BASKARA
a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))
delta = (b**2) - ((4*a)*c)
print('Valor de Delta: {}'.format(delta))
delta_r = delta ** 0.5
x1 = (-b + delta_r) / (2*a)
x2 = (-b - delta_r) / (2*a)
print('Valor de x1: {:.2f} ---- Valor de x2: {:.2f}'.format(x1,x2))