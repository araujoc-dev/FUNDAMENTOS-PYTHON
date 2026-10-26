# Escreva um programa em Python para calcular o valor de uma prestação em atraso (prestacao). 
# Para isso, obtenha o valor da prestação (valorPrestacao), a porcentagem de multa pelo atraso (multa) e a quantidade de dias de atraso (qtdeDias). 
# Calcular e mostrar o valor da prestação atualizado, sabendo que.
# prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)
valor_prestacao = float(input('Qual o valor da prestação?'))
multa = float(input('Qual o valor da multa por dia?'))
qnt_dias = int(input('Qual a quantidade de dias em atraso?'))
prestacao = valor_prestacao+(valor_prestacao*(multa/100)*qnt_dias)
print(prestacao)