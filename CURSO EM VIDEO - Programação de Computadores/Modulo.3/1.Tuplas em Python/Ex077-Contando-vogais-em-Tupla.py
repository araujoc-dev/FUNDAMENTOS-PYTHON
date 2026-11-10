times=('Milan', 'Bayern','Barcelona', 'Boca Juniors', 'Inter de Milão', 'Nacional', 'Peñarol', 'São Paulo', 'Ajax', 'Corinthians', 'Juventus',' Manchester United', 'Porto', 'Santos' , 'Chelsea')
for p in times:
    print(f'\nNa palavra {p} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print (letra, end=' ')