lnum = []
resp = " "
while True:
    num = int(input("Digite um valor: "))
    if num not in lnum:
        lnum.append(num)
        print("Novo Numero Registrado!")
    else:
        print("Numero Já Registrado!")
    while resp not in "SN":
        resp = str(input("Continuar? [S/N]")).upper().strip()[0]
    if resp in "N":
        break
    resp = " "
lnum.sort()
print(f"Valores digitados: {lnum}")
