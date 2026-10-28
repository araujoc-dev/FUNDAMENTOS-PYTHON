n1=cont=soma=0
n1 = int(input("[999 to stop] Digite um numero: "))
while n1 != 999:
    soma+=n1
    cont+=1
    n1 = int(input("[999 to stop] Digite um numero: "))
print(f"Você digitou {cont} numeros e a soma foi: {soma}")