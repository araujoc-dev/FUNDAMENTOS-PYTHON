import math
angulo=float(input("Digite um angulo: "))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f"O angulo de {angulo} tem o SENO:{seno:.2f}. Cosseno:{cos:.2f}. Tangente:{tan:.2f}.")