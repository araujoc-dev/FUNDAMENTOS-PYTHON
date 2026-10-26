# Crie um algoritmo que solicite ao usuário o seu turno de trabalho e a quantidade de horas trabalhadas, 
# calcule e mostre o valor do salário. Considere os valores de horas a seguir, de acordo com o turno de trabalho. 
# Caso o turno seja igual a ‘N’ (utilize um caractere para representar) o valor da hora trabalhada é R 45,00,casocontrárioéR  37,50.
print('TURNOS: Manhã, Tarde, Noite')
turno_job = str(input('Digite o turno o turno:'))[0].upper()
horas = float(input('Horas trabalhadas:'))
if turno_job == 'N':
  salario_hora = 45.00
else:
  salario_hora = 37.50
print(f'{horas*salario_hora} Total a receber.')