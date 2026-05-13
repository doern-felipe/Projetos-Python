# Exercícios

# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para
# determinar se o número é par ou ímpar.

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para
# classificar a idade em categorias de acordo com as seguintes condições:

#     Criança: 0 a 12 anos;
#     Adolescente: 13 a 18 anos;
#     Adulto: acima de 18 anos.

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o
# nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if
# elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo
# com as seguintes condições:

#     Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#     Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#     Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#     Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#     Caso contrário: o ponto está localizado no eixo ou origem.

# --- --- --- --- ---

# 1
def exercicio_1():
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')
exercicio_1()

# 2
def exercicio_2():
    idade = int(input('Digite sua idade: '))
    if idade >= 0 and idade <= 12:
        print('Criança.')
    elif idade >= 13 and idade <= 18:
        print('Adolescente.')
    else:
        print('Adulto.')
exercicio_2()

# 3
def exercicio_3():
    nome_usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')
    if nome_usuario == 'admin' and senha == '1234':
        print('Login bem-sucedido!')
    else:
        print('Nome de usuário ou senha incorretos.')
exercicio_3()

# 4
def exercicio_4():
    x = float(input('Digite a coordenada x: '))
    y = float(input('Digite a coordenada y: '))
    if x > 0 and y > 0:
        print('O ponto está no Primeiro Quadrante.')
    elif x < 0 and y > 0:
        print('O ponto está no Segundo Quadrante.')
    elif x < 0 and y < 0:
        print('O ponto está no Terceiro Quadrante.')
    elif x > 0 and y < 0:
        print('O ponto está no Quarto Quadrante.')
    else:
        print('O ponto está localizado no eixo ou origem.')
exercicio_4()