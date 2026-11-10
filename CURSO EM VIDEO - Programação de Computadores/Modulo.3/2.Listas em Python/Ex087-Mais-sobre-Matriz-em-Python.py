matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapar = maior = somaco = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}], [{c}]: "))
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end="")
        if matriz[l][c] % 2==0:
            somapar+=matriz[l][c]
    print()
print(f"A soma dos valores pares é {somapar}.")
for l in range(0,3):
    somaco+=matriz[l][2]
print(f"A soma dos valores da terceira coluna é {somaco}.")
for c in range(0,3):
    if maior < matriz[1][c]:
        maior=+matriz[1][c]
print(f"O Maior valor da seguda linha é {maior}")