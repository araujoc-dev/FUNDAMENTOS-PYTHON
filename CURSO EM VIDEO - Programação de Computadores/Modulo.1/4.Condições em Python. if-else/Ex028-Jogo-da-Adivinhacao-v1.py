import random
num1=random.randint(0,5)
num2=int(input("Que numero eu pensei de 0 a 5?: "))
if num2==num1:
    print(f"Acertou! Pensei no {num1}")
else:
    print(f"Errou! Pensei no {num1}")
