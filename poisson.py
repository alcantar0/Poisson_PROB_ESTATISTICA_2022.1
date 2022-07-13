#Pedro Henrique de Sousa Alcântara 13-07-22
from math import e, factorial, sqrt

lam_bda = float(input("Digite o λ (Número que corresponde ao número de ocorrências que se espera dentro de um intervalo de tempo): "))

x = int(input("Digite a variável aleatória (o número de vezes que, dentro de um certo intervalo, um evento ocorre): "))


#Poisson
vetor_de_probabilidades=[]
for i in range(0, x+1):
	vetor_de_probabilidades.append(pow(e, -lam_bda)*pow(lam_bda, i)/factorial(i))

print(f"A probabilidade de X={x}: {vetor_de_probabilidades[x]}")

print(f"Probabilidade de X>{x}: {1-sum(vetor_de_probabilidades)}")

print(f"A probabilidade de X<{x}: {sum(vetor_de_probabilidades[0:x])}")

print(f"A probabilidade de X>={x}: {1-sum(vetor_de_probabilidades[0:x])}")

print(f"A probabilidade de X<={x}: {1-(1-sum(vetor_de_probabilidades))}")

#Créditos e Fontes:
#https://www.laboneconsultoria.com.br/distribuicao-de-poisson/#A-Distribui%C3%A7%C3%A3o-de-Poisson


