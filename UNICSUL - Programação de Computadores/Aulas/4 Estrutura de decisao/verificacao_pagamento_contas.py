# Escreva um programa em Python que solicite ao usuário os valores de três contas de consumo (p.ex. água, luz e telefone) e o valor de seu salário. 
# Verifique se o salário é suficiente para pagar as três contas, caso não seja apresente a mensagem “Salário insuficiente!”. 
# Caso seja, apresente o valor que restou do salário após pagar as contas.
agua = float(input('Valor da Conta de agua: '))
luz = float(input('Valor da Conta de luz: '))
tele = float(input('Valor da Conta de telefone: '))
salario = float(input('Digite seu salario: '))
total_conta = agua+luz+tele
if salario >= total_conta:
  print(f'Salario restante: {salario-total_conta} // Contas Pagas.')
else:
  print('Salário insuficiente.')