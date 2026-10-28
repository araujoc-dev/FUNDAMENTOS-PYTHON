casavalor=float(input("Valor da casa: "))
salario=float(input("Salário do comprador: "))
financia=float(input("Quantos anos de financiamento: "))
presta=casavalor/(financia*12)
print(f"Para pegar uma casa de {casavalor:.2f} em {financia} anos a prestação será de {presta:.2f}")
if presta > salario*0.3:
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo CONCEDIDO!")