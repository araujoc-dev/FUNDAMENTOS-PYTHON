salario=float(input("Valor do salário atual: "))
if salario > 1250:
    print(f"Quem ganhava R${salario:.2f} passa a ganhar {(salario*0.10)+salario:.2f}")
else:
    print(f"Quem ganhava R${salario:.2f} passa a ganhar {(salario*0.15)+salario:.2f}")