# 3.2 Declarar uma lista e imprimir somente o primeiro e último valor da lista
from array import ArrayType


resp = 's'
soma = quantidade = media = 0
while resp in 'Ss':
    num = int(input('digite um numero: '))
    soma += num
    quantidade += 1
    resp=str(input('quer continuar? [S/N] ')).upper().strip()[0]
media=soma/quantidade
print('Você digitou {} numeros e a media foi {}'.format(quantidade,media))