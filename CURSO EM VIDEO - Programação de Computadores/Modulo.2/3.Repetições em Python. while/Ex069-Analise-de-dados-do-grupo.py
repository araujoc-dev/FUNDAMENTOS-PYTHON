tot18=totH=totM20=0
while True:
    print(f"{"=-="*10}\nCADASTRO DE PESSOA\n{"=-="*10}")
    idade=int(input("Idade: "))
    sexo=" "
    while sexo not in "FM":
        sexo=str(input("Sexo: [M/F]")).upper().strip()[0]
    if idade>=18:
        tot18+=1
    if sexo == "M":
        totH+=1
    if sexo == "F" and idade < 20:
        totM20+=1
    resp=" "
    while resp not in "SN":
        resp= str(input("Continuar? [S/N]")).upper().strip()[0]
    if resp == "N":
        break
print(f"Total de pessoas +18: {tot18}\nHomens: {totH}\nMulheres -20 Anos: {totM20}")

