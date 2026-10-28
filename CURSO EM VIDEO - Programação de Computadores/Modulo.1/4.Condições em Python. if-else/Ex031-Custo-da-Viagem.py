viagemd=int(input("Qual a distancia da viagem? Km: "))
valor=0
if viagemd <= 200:
    valor=0.50
else:
    valor=0.45
print(f"Valor da sua viagem ficará: R${viagemd*valor:.2f}")