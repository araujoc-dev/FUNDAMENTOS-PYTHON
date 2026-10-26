# Escreva um programa em Python que solicite ao usuário o salário atual e mostre o salário acrescido de 5% de comissão.
salario = float(input('Qual o seu salario? '))
resultado_porce =  salario+(salario * 0.05)
print('Salario acrescido R${}'.format(resultado_porce))