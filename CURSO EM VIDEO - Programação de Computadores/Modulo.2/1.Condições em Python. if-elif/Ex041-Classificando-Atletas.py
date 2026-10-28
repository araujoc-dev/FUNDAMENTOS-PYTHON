from datetime import date
hj=date.today().year
nasce=int(input("Ano de Nascimento: "))
idade = hj - nasce
print(f"Atleta tem {idade} anos.")
if idade <= 9:
    print("Classificação: MIRIM.")
elif idade <=14:
    print("Classificação: INFANTIL.")
elif idade <=19:
    print("Classificação: JÚNIOR.")
elif idade <=25:
    print("Classificação: SÊNIOR.")
else:
    print("Classificação: MASTER.")