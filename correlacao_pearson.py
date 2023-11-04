# Determinando o coeficiente de correlação de Pearson

# DESCRIÇÃO PARA O USUÁRIO

print(" ")
print("Projeto em Sistemas Inteligentes")
print(" ")
print("Direção: Prof° Sergio João Guimaraes Da Silva")
print(" ")
print("Método de Pearson")
print(" ")

# DADOS DO USUÁRIO

x1 = float(input('Digite o valor de X: '))
x2 = float(input('Digite o valor de X: '))
x3 = float(input('Digite o valor de X: '))
x4 = float(input('Digite o valor de X: '))
x5 = float(input('Digite o valor de X: '))
x6 = float(input('Digite o valor de X: '))
y1 = float(input('Digite o valor de Y: '))
y2 = float(input('Digite o valor de Y: '))
y3 = float(input('Digite o valor de Y: '))
y4 = float(input('Digite o valor de Y: '))
y5 = float(input('Digite o valor de Y: '))
y6 = float(input('Digite o valor de Y: '))
total_linhas = 6

# MONTANDO AS COLUNAS

# Somando os valores de X

xi = x1 + x2 + x3 + x4 + x5 + x6

# Somando os valores de Y

yi = y1 + y2 + y3 + y4 + y5 + y6

# Calculando a média do X

x_media = xi / total_linhas

# Calculando a média do Y

y_media = yi / total_linhas

# Subtraindo o Xi - x_media

x1_m = x1 - x_media
x2_m = x2 - x_media
x3_m = x3 - x_media
x4_m = x4 - x_media
x5_m = x5 - x_media
x6_m = x6 - x_media

# Somando os resultados de xi - x_ media

xi_m_soma = x1_m + x2_m + x3_m + x4_m + x5_m + x6_m

# Subtraindo o Yi - y_media

y1_m = y1 - y_media
y2_m = y2 - y_media
y3_m = y3 - y_media
y4_m = y4 - y_media
y5_m = y5 - y_media
y6_m = y6 - y_media

# Somando os resultados de yi - y_ media

yi_m_soma = y1_m + y2_m + y3_m + y4_m + y5_m + y6_m

# Multiplicando os resultados de X média * Y média

m_x1y1 = x1_m * y1_m
m_x2y2 = x2_m * y2_m
m_x3y3 = x3_m * y3_m
m_x4y4 = x4_m * y4_m
m_x5y5 = x5_m * y5_m
m_x6y6 = x6_m * y6_m

# Somando os resultados multiplicados

xy_soma = m_x1y1 + m_x2y2 + m_x3y3 + m_x4y4 +m_x5y5 + m_x6y6

# Calculando o resultado da media de X elevado ao quadrado

x1_m_e = x1_m ** 2
x2_m_e = x2_m ** 2
x3_m_e = x3_m ** 2
x4_m_e = x4_m ** 2
x5_m_e = x5_m ** 2
x6_m_e = x6_m ** 2

# Somando os resultados de x^2

xe_soma = x1_m_e + x2_m_e + x3_m_e + x4_m_e + x5_m_e + x6_m_e

# Calculando o resultado da media de Y elevado ao quadrado

y1_m_e = y1_m ** 2
y2_m_e = y2_m ** 2
y3_m_e = y3_m ** 2
y4_m_e = y4_m ** 2
y5_m_e = y5_m ** 2
y6_m_e = y6_m ** 2

# Somando os resultados de Y^2

ye_soma = y1_m_e + y2_m_e + y3_m_e + y4_m_e + y5_m_e + y6_m_e

# Resolvendo a fórmula

multi = xe_soma * ye_soma
raiz = pow(multi, 0.5)
resultadoo = xy_soma / raiz
resultado = float(resultadoo)

# Condição se o resultado for = 0

if raiz == 0:
    print("Não é possível dividir por zero")
    print(" ")
    print("Grupo: Jéssica de Jesus Da Silva ")
    print("       Tamires Dionizia De Jesus Benardes ")
    print("       Lavínia De Souza Freitas ")
    print("       Marina Romera Amorim ")
    print("       Riani Katelin Da Silva ")
    print(" ")
    input("Para sair aperte 'Enter'")


# Exibindo o resultado final

print(" ")
print("Calculando....")
print(" ")
print("O coeficiente da correlação de Pearson entre X e Y é: ", resultado)

print(" ")
print("Grupo: Jéssica de Jesus Da Silva ")
print("       Tamires Dionizia De Jesus Benardes ")
print("       Lavínia De Souza Freitas ")
print("       Marina Romera Amorim ")
print("       Riani Katelin Da Silva ")
print(" ")
input("Para sair aperte 'Enter'")
