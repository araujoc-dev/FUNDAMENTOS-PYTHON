frase=str(input("Digite um texto: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso= junto[::-1]
if inverso == junto:
    print("Temos um palindromo!")
else:
    print("A drase não é palindromo")
print(f"Você digitou a frase {inverso}")
