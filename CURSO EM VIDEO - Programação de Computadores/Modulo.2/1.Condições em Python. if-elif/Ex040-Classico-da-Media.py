nota1=float(input("Primeira nota: "))
nota2=float(input("Segunda nota: "))
media = (nota1+nota2)/2
if media < 5:
    print(f"Sua média foi: {media}. REPROVADO!")
elif media >= 5 and media <=6.9:
    print(f"Sua média foi: {media}. RECUPERAÇÃO!")
elif media >= 7:
    print(f"Sua média foi: {media}. APROVADO!")