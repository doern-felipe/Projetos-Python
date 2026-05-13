# Exercícios

# 1 - Crie uma lista para cada informação a seguir:

#     Lista de números de 1 a 10;
#     Lista com quatro nomes;
#     Lista com o ano que você nasceu e o ano atual.

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a
# tabuada desse número, indo de 1 a 10.

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os
# elementos. Utilize um bloco try-except para lidar com possíveis exceções.

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco
# try-except para lidar com a divisão por zero, caso a lista esteja vazia.

# --- --- --- --- ---

# 1
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ["Alice", "Bob", "Charlie", "David"]
anos = [2007, 2026]

# 2
for numero in numeros:
    print(numero)

# 3
soma_impares = 0
for numero in numeros:
    if numero % 2 != 0:
        soma_impares += numero
print(soma_impares)

# 4
for numero in numeros[::-1]:
    print(numero)

# 5
numero = int(input('Digite um número para ver sua tabuada: '))
for i in range(1,11):
    print(f'{numero} x {i} = {numero * i}')

# 6
numeros = [1, 2, 3, 4, 5]
soma = 0
try:
    for numero in numeros:
        soma += numero
    print(f'A soma dos números é: {soma}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')

# 7
numeros = [1, 2, 3, 4, 5]
soma = sum(numeros)
try:
    media = soma / len(numeros)
    print(f'A média dos números é: {media}')
except ZeroDivisionError:
    print('A lista está vazia, não é possível calcular a média.')