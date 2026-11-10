valores = []
while True:
    valores.append(int(input("Digite um valor: ")))
    resp = str(input("Deseja continuar? "))
    if resp in 'Nn':
        break
print(f"Foram digitados {len(valores)}.")
valores.sort(reverse=True)
print(f"Valores em ordem decrescente {valores}")
if 5 in valores:
    print("O numero 5 está nos valores.")
else:
    print("O numero 5 não está nos valores.")