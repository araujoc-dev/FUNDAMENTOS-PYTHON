# Escreva um programa em Python que solicite ao usuário a distância entre duas cidades e o tempo de viagem. 
# O programa deverá calcular e exibir a velocidade média de um carro que vai de uma cidade para outra. Utilize a fórmula: VM:DISTANCIA/TEMPO
distancia = float(input('Qual a distancia em KM?'))
tempo = float(input('Qual o tempo de viagem em Horas?'))
velomedia = distancia / tempo
print('A media de velocidade do carro é {}KM/h'.format(velomedia))