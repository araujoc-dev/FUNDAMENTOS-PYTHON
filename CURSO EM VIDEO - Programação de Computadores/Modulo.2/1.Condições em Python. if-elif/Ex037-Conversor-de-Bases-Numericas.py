num=int(input("Digite um numero inteiro: "))
print("Escolha uma das bases para conversão:\n[1] Converter para BINÁRIO.\n[2] Converter para OCTAL.\n[3] Converter para HEXADECIMAL.")
opcao=int(input("Sua opção: "))
if opcao==1:
    print(f"{num} Convertido em Binário: {bin(num)}")
elif opcao==2:
    print(f"{num} Convertido em Binário: {oct(num)}")
elif opcao==3:
    print(f"{num} Convertido em Binário: {hex(num)}")
else:
    print("Opçao Inválida!")