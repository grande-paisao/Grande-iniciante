# Grande-iniciante
# 1. Utilize uma variavel para imprimir "Hello World"
vari="Hello word"
print(vari)

#2. Receber dois números do usuario e somar
#3. Receber dois números do usuario e multiplicar
print(5+8)
nu1=5
nu2=8
nu3=1
nu4=1
nu5=1
soma=(nu1+12+nu2+nu3+nu4+nu5)
print(soma*2)

# 4. Receber dois números do usuario e verificar se são iguais
igual=2
igual2=2
if(igual==igual2):
       print("os numeros são igual!!!")
else:
    print("os numeros são diferentes!!!")
    
#5. Receber dois números do usuario e somar
a= "Denis"
b= "Cezar"
c= " Ribeiro"
nome= a+b+c
print(nome)
print(nome,"tem 15 anos")
a1="oi"
b1=' tudo bem'
c1=' como está, '
d1='sou Denis tenho 15 anos'
e1=" e"
f=" trabalho aqui."
g=(a1+b1+c1+d1+e1+f)
print(g)

#6.Printar uma lista usando for
list=['denis','666','?????','<3<3<3<3','mas bah']
for nome in list:
    print(nome)
    
#1.2 Receber dados do usuário usar o input()
print('Enter your name:')
x = input()
print('Hello, ' + x)

# 2.2 Receber dois números do usuário e ver qual dos dois é maior'''
num1 = int (input('Primeiro numero: '))

num2 = int(input('Segundo numero: '))

if num1 > num2:
    print(num1 ('primeiro é maior'))
else:
    print(num2)
    
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

# 3/2.2 Declarar uma lista e imprimir somente o primeiro e último valor da lista
nome=['denis','666','?????','<3<3<3<3','mas bah']
tamanholista=len(nome)
print('O primeiro valor é: '+ nome[0])
print('Ultimo valor é: '+ nome[tamanholista-1])
print('o tamanho da lista é: ' ,tamanholista)

# 4.2 Receber um nome do usuário e trocar as letras A por B
nome=input('Digite seu nome: ')
nomeinvertido= nome.replace('e','i')

print('o seu nome normal é:' + nome)
print('o seu nome invertido é: ' + nomeinvertido)

# 5.2 Receber 3 numeros do usuario e imprimir em ordem crescente
num=[]
num1= int (input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
num3 = int(input('Terceiro numero: '))
num.append(num1)
num.append(num2)
num.append(num3)
num.sort()
print(num)

