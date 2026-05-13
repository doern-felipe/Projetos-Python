# Exercícios

# 1 - Imprima a frase: Python na Escola de Programação da Alura.

# 2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores
# armazenados em variáveis.

# 3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:

# A
# L
# U
# R
# A

# 4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser
# armazenado em uma variável e arredondado para apenas duas casas decimais.
# Para facilitar, utilize: pi = 3.14159

# --- --- --- --- ---

# 1
def exercicio_1():
    print('Python na Escola de Programação da Alura.')
exercicio_1()

# 2
def exercicio_2():
    nome = "Felipe"
    idade = 18
    print(f"Meu nome é {nome} e tenho {idade} anos.")
exercicio_2()

# 3
def exercicio_3():
    print('A\nL\nU\nR\nA')
exercicio_3()

# 4
def exercicio_4():
    pi = 3.14159
    pi_arredondado = f"{pi:.2f}"
    print(f"O valor arredondado de pi é: {pi_arredondado}")
exercicio_4()