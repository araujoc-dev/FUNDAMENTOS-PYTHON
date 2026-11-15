MediaAl=dict()

MediaAl['nome']=str(input("Nome: "))
MediaAl['media']=float(input(f"Média de {MediaAl['nome']}: "))

if MediaAl['media'] < 5:
    MediaAl['status'] = 'Reprovado.'
elif 5 <= MediaAl['media'] < 7:
    MediaAl['status'] = 'Recuperação.'
else:
    MediaAl['status'] = 'Aprovado.'
print("*"*45)
for k, v in MediaAl.items():
    print(f"{k.title()}: {v}")