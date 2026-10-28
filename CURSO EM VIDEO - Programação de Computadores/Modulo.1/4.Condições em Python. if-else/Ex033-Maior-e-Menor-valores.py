num1=int(input("Primeiro valor: "))
num2=int(input("Segundo valor: "))
num3=int(input("Terceiro valor: "))
men=num1
mio=num3
if num2<num1 and num2<num3:
    men=num2
if num3<num2 and num3<num1:
    men=num3
if num2>num1 and num2>num3:
    mio=num2
if num3>num2 and num3>num1:
    mio=num3

print(f"O maior:{mio}. O menor:{men}")