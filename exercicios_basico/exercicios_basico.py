"""
  Faça um programa que peça ao usuário para digitar um número inteiro, 
  informe se estenúmero é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

"""
# entrada = input('Digite um numero: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O numero {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um numero inteiro')

"""
  Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
  exiba a saudação apropriada. Ex. 
  Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""
entrada = input('Digite a hora em nuemros: ')

try:
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print('Olá!, Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Olá!, Boa Tarde')
    elif hora >= 18 and hora <= 23:
        print('Olá!, Boa Noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas numeros inteiros')

"""
  Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".

"""
