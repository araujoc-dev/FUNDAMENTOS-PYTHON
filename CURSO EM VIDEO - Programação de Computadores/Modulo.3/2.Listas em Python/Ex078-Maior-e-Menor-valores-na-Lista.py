numeros = []
mai = men = 0
pmai = []
pmen = []
for n in range(5):
    numeros.append(int(input(f'Digite um valor para a Posição {n}: ')))
    if n == 0:
        mai = men = numeros[0]
    else:
        if numeros[n] > mai:
            mai = numeros[n]
        if numeros[n] < men:
            men = numeros[n]
for i, v in enumerate(numeros):
    if v == mai:
        pmai.append(i)
    if v == men:
        pmen.append(i)
print(f"Você digitou os valores {numeros}\nO Maior valor digitado foi {mai} Posição: {pmai} \nO Menor valor digitado foi {men} Posição: {pmen}")

