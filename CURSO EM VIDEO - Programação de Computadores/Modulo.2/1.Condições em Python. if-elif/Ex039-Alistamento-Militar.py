from datetime import date
hj=date.today().year
nasce=int(input("Ano de Nascimento: "))
idade = hj - nasce
print(f"Quem nasceu em {nasce} tem {idade} anos em {hj}")
if idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!")
elif idade < 18:
    saldo = 18-idade
    print(f"Você ainda tem 18 anos. Faltam {saldo} anos para o alistamento.")
elif idade > 18:
    saldo= idade-18
    print(f"Você já deveria ter se alistado há {saldo} anos.")
