# Escreva um programa em Python que leia um valor representando o gasto realizado por um cliente do restaurante ComaBem 
# Visualize o valor total a ser pago, considerando os 10% do garçom.
conta = float(input('Valor da conta: '))
gorjeta = (conta * 0.1) + conta
print('Valor total da conta: R${}'.format(gorjeta))