velo=int(input("Qual a velocidade atual do carro? "))
if velo<80:
    print("Tenha um bom dia! Dirija com segurança!")
else:
    print(f"Multado! Voce excedeu o limite permitido de 80Km/h\nVocê deve pagar uma multa de R${(velo-80)*7:.2f}!")