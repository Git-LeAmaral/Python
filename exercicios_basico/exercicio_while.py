"""
  Iterando Strings com while

"""
nome = 'Leandro'

indice = 0 
novo_nome = ''

while indice < len(nome):
    print(nome[indice])
    letra = nome[indice]
    novo_nome += f'#{letra}'
    indice += 1

    print(novo_nome)