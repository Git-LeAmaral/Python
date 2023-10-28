# Bem-vindo ao programa de cálculo de IMC!

# O IMC é uma medida da proporção entre o peso e a altura de uma pessoa. É usado para classificar o estado nutricional de uma pessoa.

# Para calcular o seu IMC, informe seu peso em kg e sua altura em m.

peso = float(input("Qual é o seu peso (em kg)? "))
altura = float(input("Qual é a sua altura (em m)? "))

# O IMC é calculado usando a seguinte fórmula:

imc = peso / altura ** 2

# O IMC é classificado da seguinte forma:

# * Abaixo do peso: IMC < 18,5
# * Peso normal: IMC >= 18,5 e IMC < 25
# * Sobrepeso: IMC >= 25 e IMC < 30
# * Obesidade grau 1: IMC >= 30 e IMC < 35
# * Obesidade grau 2: IMC >= 35 e IMC < 40
# * Obesidade grau 3: IMC >= 40

# Seu IMC é {:.2f}.

print("Seu IMC é {:.2f}.".format(imc))

# Classificação do IMC:

if imc < 18.5:
  print("Abaixo do peso")
elif imc < 25:
  print("Peso normal")
elif imc < 30:
  print("Sobrepeso")
elif imc < 35:
  print("Obesidade grau 1")
elif imc < 40:
  print("Obesidade grau 2")
else:
  print("Obesidade grau 3")