maiorpeso = 0
menorpeso = 0
for i in range(1,5):
    peso = float(input(f"Peso da {i} pessoa: "))
    if i == 1:
        maiorpeso=peso
        menorpeso=peso
    if maiorpeso < peso:
        maiorpeso = peso
    if menorpeso > peso:
        menorpeso = peso
print(f"O maior peso foi {maiorpeso}Kg e o menor foi {menorpeso}Kg.")