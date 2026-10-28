from random import randint
chute = 0
tentativa = 0
num = randint(1,5)
print("Pensei em um numero entre 1 a 10.")
while num != chute:
    chute=int(input("Chute um numero: "))
    tentativa+=1
    if num > chute:
        print("Mais... Tente novamente!")
    elif num < chute:
        print("Menos... Tente novamente!")
print(f"Acertou pensei no {num}! Tentativas: {tentativa}")