# Faça uma programa em Python que peça do usuário um valor em graus para um ângulo. 
# Converta-o para radianos e, usando funções da biblioteca math, imprima o seno, cosseno e tangente deste ângulo.
import math
angulo = float(input('Digite o ângulo:'))
angulo_r = math.radians(angulo)
cos = math.cos(angulo_r)
seno = math.sin(angulo_r)
tan = math.tan(angulo_r)
print(f'{angulo:.2f}Angulo.\n{angulo_r:.2f} Angulo Radiano.\n{tan:.2f} Tangente.\n{seno:.2f} Seno.\n{cos:.2f} Cosseno.')