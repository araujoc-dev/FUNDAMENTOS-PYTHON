altura=float(input("Qual sua Altura (m): "))
peso=float(input("Qual seu Peso (Kg): "))
imc=peso/(altura*altura)
if imc <18.5:
    print("Abaixo do peso.")
elif imc<=25:
    print("Peso Ideal.")
elif imc<=30:
    print("Sobrepeso.")
elif imc<=40:
    print("Obesidade.")
else:
    print("Obesidade Mórbida.")