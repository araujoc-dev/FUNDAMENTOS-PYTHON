n1=int(input("Primeiro Valor: "))
n2=int(input("Segundo Valor: "))
opcao=0
while opcao!=5:
    print("======================\n[ 1 ] Somar.\n[ 2 ] Multiplicar.\n[ 3 ] Maior.\n[ 4 ] Novos Números.\n[ 5 ] Sair do programa.\n======================")
    opcao=int(input("Escolha uma opção: "))
    if opcao == 1:
        soma=n1+n2
        print(f"Soma de: {n1}+{n2}={soma}")
    elif opcao ==2:
        mult=n1*n2
        print(f"Multiplicação de: {n1}x{n2}={mult}")
    elif opcao ==3:
        if n1 > n2:
            maior=n1
        else:
            maior=n2
        print(f"Maior de : {n1} e {n2} é {maior}")
    elif opcao ==4:
        n1=int(input("Primeiro Valor: "))
        n2=int(input("Segundo Valor: "))
print("Programa encerrado!")
 