# REGRESSÃO LINEAR

# DESCRIÇÃO PARA O USUÁRIO

print(" ")
print("Projeto em Sistemas Inteligentes")
print(" ")
print("Direção: Prof° Sergio João Guimaraes Da Silva")
print(" ")
print("Regressão Linear")
print(" ")

# DADOS DO USUÁRIO

a = float(input('Digite o valor de X: '))
b = float(input('Digite o valor de X: '))
c = float(input('Digite o valor de X: '))
d = float(input('Digite o valor de X: '))
e = float(input('Digite o valor de X: '))
f = float(input('Digite o valor de X: '))
g = float(input('Digite o valor de X: '))
h = float(input('Digite o valor de X: '))
i = float(input('Digite o valor de X: '))
j = float(input('Digite o valor de X: '))
k = float(input('Digite o valor de f(x): '))
l = float(input('Digite o valor de f(x): '))
m = float(input('Digite o valor de f(x): '))
n = float(input('Digite o valor de f(x): '))
o = float(input('Digite o valor de f(x): '))
p = float(input('Digite o valor de f(x): '))
q = float(input('Digite o valor de f(x): '))
r = float(input('Digite o valor de f(x): '))
s = float(input('Digite o valor de f(x): '))
t = float(input('Digite o valor de f(x): '))
quantidade = float(input("Digite a quantidade de linhas: "))

# MULTIPLICANDO OS VALORES DE X e F(x) PARA OBTER O VALOR DE x*f(x)

# Valores de x = a até j
# Valores de f(x) = k até t

ak = a * k
bl = b * l
cm = c * m
dn = d * n
eo = e * o
fp = f * p
gq = g * q
hr = h * r
iss = i * s
jt = j * t

# CALCULANDO OS VALORES DE X ELEVADO AO QUADRADO PARA OBTER O X^2

a2 = a ** 2
b2 = b ** 2
c2 = c ** 2
d2 = d ** 2
e2 = e ** 2
f2 = f ** 2
g2 = g ** 2
h2 = h ** 2
i2 = i ** 2
j2 = j ** 2

# SOMATORIA DE x, f(x), x*f(x) e x^2

xs = a + b + c + d + e + f + g + h + i + j
fxs = k + l + m + n + o + p + q + r + s + t
xfxs =  ak + bl + cm + dn + eo + fp + gq + hr + iss + jt
x2s = a2 + b2 + c2 + d2 + e2 + f2 + g2 + h2 + i2 + j2


# CALCULANDO O VALOR DE A

valor_A = (xs * xfxs - x2s * fxs) / (xs**2 - quantidade * x2s)

# CALCULAMDO O VALOR DE B

valor_B = (xs * fxs - quantidade * xfxs) / (xs**2 - quantidade * x2s)

# EXIBINDO O RESULTADO FINAL

print(" ")
print("Calculando....")
print(" ")
print(f'Valor de A: {valor_A}')
print(f'Valor de B: {valor_B}')
print(" ")
print("Grupo: Jéssica de Jesus Da Silva ")
print("       Tamires Dionizia De Jesus Benardes ")
print("       Lavínia De Souza Freitas ")
print("       Marina Romera Amorim ")
print("       Riani Katelin Da Silva ")
print(" ")
input("Para sair aperte 'Enter'")
print(" ")
