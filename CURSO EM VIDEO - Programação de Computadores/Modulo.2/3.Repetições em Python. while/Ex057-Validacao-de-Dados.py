sexo= str(input("Informe seu sexo: [M/F]" )).upper()[0].strip()
while sexo not in "MF":
    sexo= str(input("Sexo Inválido! Informe seu sexo: [M/F]" )).upper()[0].strip()
print(f"Sexo {sexo} Registrado com sucesso!")
