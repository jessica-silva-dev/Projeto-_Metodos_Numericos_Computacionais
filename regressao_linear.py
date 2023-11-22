# REGRESSÃO LINEAR

from time import sleep
from colorama import Fore, Style, init
init()

# DEFININDO AS VARIÀVEIS DAS CORES

verde = Fore.LIGHTGREEN_EX
azul = Fore.BLUE
branco = Fore.LIGHTWHITE_EX
amarelo = Fore.LIGHTYELLOW_EX
verde_agua = Fore.LIGHTCYAN_EX
laranja = Fore.LIGHTRED_EX
reset = Style.RESET_ALL

# DESCRIÇÃO PARA O USUÁRIO

print(" ")
print(f"{branco}Projetos em Sistemas Inteligentes{reset}")
sleep(2)
print(" ")
print(f"{branco}Direção:Prof° Sergio João Guimaraes Da Silva{reset}")
sleep(2)
print(" ")
print(f"{branco}Método: Regressão Linear{reset}")
sleep(2)
print(" ")

# Criando as lista
x = []
fx = []
m = int(input(f"{verde_agua}Informe a quantidade de linhas: {reset}"))

# Criando um loop para pegar os dados do usuário.
# Condição de parada do loop, se o usuário já colocou os valores, é somente digitar 00 no x e f(x) que vai parar de pedir valores.

for i in range(m):
    a = float(input(f"{verde_agua}Informe o valor de X: {reset}"))
    b = float(input(f"{verde_agua}Informe o valor de f(x): {reset}"))
    x.append(a)
    fx.append(b)

# Multiplicando os valores de X e F(x) para obter a coluna de x*f(x)
# Criando a lista que vai receber os resultados da multiplicação

coluna_xfx = []

# Fazendo a multiplicção das colunas
# Função zip é para fazer essa interação entre listas diferentes
# Ou seja ela pegou os resultados multiplicados e formou uma nova lista(coluna)

for mult_x, mult_fx in zip(x, fx):
    multiplicar = mult_x * mult_fx
    coluna_xfx.append(multiplicar)
       
# Calculando os valores de X elevado ao quadrado para obter a coluna de X^2
# Criando lista que vai receber os resultados de x elevado ao quadrado

coluna_xelevado2 = []

# Aqui não usei a função zip, pois estamos ultilizando somente a lista de X

for elevado in x:
    elevar = elevado ** 2
    coluna_xelevado2.append(elevar)

# SOMATORIA DE x, f(x), x*f(x) e x^2

# Criando as variáveis que vai receber os valores das listas
# Ela começa com zero, para não interferir nos resultados.

soma_x = 0
soma_fx = 0
soma_xfx = 0
soma_x2 = 0

# Usando novamente a função, pois estamos mexendo com várias listas

for sx, sfx, sxfx, sx2 in zip(x, fx, coluna_xfx, coluna_xelevado2):
    soma_x += sx
    soma_fx += sfx
    soma_xfx += sxfx
    soma_x2 += sx2

# CALCULANDO O VALOR DE A

valor_A = (soma_x * soma_xfx - soma_x2 * soma_fx) / (soma_x**2 - m * soma_x2)

# CALCULAMDO O VALOR DE B

valor_B = (soma_x * soma_fx - m * soma_xfx) / (soma_x**2 - m * soma_x2)

# EXIBINDO O RESULTADO FINAL

print(" ")
print(f"{laranja}Calculando ...{reset}")
print(" ")
sleep(2)
print(f"{laranja}Adquirindo Resultados ...{reset}")
print(" ")
sleep(2)
print(f"{laranja}O Resultado da Regressão Linear é: {reset}")
print(" ")
sleep(2)
valor_A_letra = str(valor_A)
valor_B_letra = str(valor_B)
print(f"f(x) = ({valor_A:.4f}) - ({valor_B:.4f}x{reset})")
print(" ")
sleep(2)
print(f"{laranja}Participantes do Grupo: {reset}")
sleep(1)
print(f"{verde}Tamires Dionizia De Jesus Bernardes --> RA: 3023200548{reset}")
sleep(1)
print(f"{verde}Jéssica De Jesus Da Silva --> RA: 3023200546{reset}")
sleep(1)
print(f"{verde}Lavínia De Souza Freitas --> RA: 3023202645{reset}")
sleep(1)
print(f"{verde}Riani Katelin Da Silva --> RA: {reset}")
sleep(1)
print(f"{verde}Marina Romera Amorim --> RA: 3023108400{reset}")
sleep(1)
print(f"{verde_agua}Créditos: Ahmad Abouleinin{reset}")
print(" ")
sleep(2)
input(f"{laranja}Para sair aperte 'Enter'!{reset}")
print(" ")
