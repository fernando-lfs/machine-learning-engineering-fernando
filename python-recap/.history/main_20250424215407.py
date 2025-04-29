# STTRINGS #

# 1 - Imprima a frase: Python na Escola de Programação da Alura.

print("Python na Escola de Programação da Alura")

# 2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.

nome = "Fernando"
idade = 31
print(f"Meu nome é {nome} e tenho {idade} anos")

# 3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:

print("A", "L", "U", "R", "A", sep="\n")

# 4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:

pi = 3.14159265358979323846
print(f"O valor arredondado de pi é: {pi:.2f}")

# CONDICIONAIS #

# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

n = int(input("Insira um número:"))
print(f"O número {n} é par") if n % 2 == 0 else print(f"O número {n} é ímpar")

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

idade = int(input("Insira sua idade:"))

if idade >= 0 and idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 18:
    print("Adolescente")
elif idade > 18:
    print("Adulto")
else:
    print("Idade invalida")


# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

login = input("Insira seu usuario:")
login_senha = input("Insira sua senha:")

user = "FLF"
passw = "1234"

print("Acesso permitido") if login == user and login_senha == passw else print(
    "Credenciais incorretas"
)


# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

coordenadas = []
coordenadas.insert(0, int(input("Insira a coordenada x:")))
coordenadas.insert(1, int(input("Insira a coordenada y:")))

if coordenadas[0] > 0 and coordenadas[1] > 0:
    print("Primeiro quadrante.")
elif coordenadas[0] < 0 and coordenadas[1] > 0:
    print("Segundo quadrante.")
elif coordenadas[0] < 0 and coordenadas[1] < 0:
    print("Terceiro quadrante.")
elif coordenadas[0] > 0 and coordenadas[1] < 0:
    print("Quarto quadrante.")
else:
    print("Eixo ou origem")


# LISTA #

# 1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)

numeros = []

for x in range(1, 11):
    numeros.append(x)

print(numeros)

# Lista com quatro nomes;

nomes = []

for i in range(4):
    nomes.append(input("Insira um nome:"))

print(nomes)

for nome in nomes:
    print(nome)

# Lista com o ano que você nasceu e o ano atual.

dados = []

dados.append(input("Ano de nascimento:"))
dados.append(input("Ano atual:"))

print(dados)

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in numeros:
    print(x)

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

soma = 0

for i in range(1, 10, 2):
    soma += i

print(soma)

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

for i in range(10, 0, -1):
    print(i)


# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero = int(input("Insira um número"))

for i in range(numero):
    print(f"{numero} x {i + 1} = {numero * (i + 1)}")

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

try:
    for numero in numeros:
        soma += numero
    print(f"A média é igual a: {soma / len(lista_numeros)}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


# DICIONÁRIO #

"""
1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
"""

dados_pessoais = {"nome": "Fernando", "idade": 31, "cidade": "Belo Horizonte"}

dados_pessoais.items()

"""
2 - Utilizando o dicionário criado no item 1:
- Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
- Adicione um campo de profissão para essa pessoa;
- Remova um item do dicionário.
"""

dados_pessoais = {"nome": "Fernando", "idade": 31, "cidade": "Belo Horizonte"}

dados_pessoais["nome"] = "Fernando Luiz Ferreira"
dados_pessoais.update({"profissao": "Analista de BD"})
dados_pessoais.pop("cidade")
dados_pessoais.items()

"""
3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
"""


"""
4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
"""


"""
5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
"""
