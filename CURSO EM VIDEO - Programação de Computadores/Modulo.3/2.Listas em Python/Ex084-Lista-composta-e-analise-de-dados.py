pessoa=list()
listap=list()
mai = men = 0
while True:
    pessoa.append(str(input("Nome: ")))
    pessoa.append(int(input("Peso: ")))
    if len(listap) == 0:
        mai = men = pessoa[1]
    else:
        if pessoa[1] > mai:
            mai = pessoa[1]
        if pessoa[1] < men:
            men = pessoa[1]
    listap.append(pessoa[:])
    pessoa.clear()
    resp = str(input("Deseja continuar? "))
    if resp in 'Nn':
        break
print(f"Ao todo, você cadastrou {len(listap)} Pessoas.")
print(listap)
for u in listap:
    if u[1] == mai:
        print(f"O maior peso foi {mai} de {u[0]}")
for u in listap:
    if u[1] == men:
        print(f"O menor peso foi {men} de {u[0]}")



