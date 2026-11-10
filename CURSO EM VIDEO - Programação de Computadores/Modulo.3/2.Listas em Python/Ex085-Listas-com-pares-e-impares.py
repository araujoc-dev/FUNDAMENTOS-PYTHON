numeros = [[],[]]
for i in range(0,8):
    num=int(input(f"Digite o {i+1} valor: "))
    if num % 2==0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f"Os valores Pares digitados foram: {numeros[0]}.\nOs valores Impares digitados foram: {numeros[1]}.")