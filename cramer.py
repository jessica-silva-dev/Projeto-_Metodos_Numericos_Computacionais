# MÉTODO DE CRAMER

# IMPORTANDO BLIBIOTECAS
from time import sleep
from colorama import Fore, Style, init

init()

# DEFININDO AS VARIÀVEIS DAS CORES
verde = Fore.LIGHTGREEN_EX
azul = Fore.BLUE
laranja = Fore.LIGHTRED_EX
amarelo = Fore.YELLOW
reset = Style.RESET_ALL

# DESCRIÇÃO PARA O USUÁRIO

print(" ")
sleep(2)
print(f"{laranja}Projeto em Sistemas Inteligentes {reset}")
print(" ")
sleep(2)
print(f"{laranja}Direção: Prof° Sergio João Guimaraes Da Silva {reset}")
print(" ")
sleep(2)
print(f"{laranja}Método: Cramer {reset}")
print(" ")
sleep(2)

# ENTRADA DE DADOS DO USUÁRIO
a = float(input(f"{azul}Digite o valor de X: {reset}"))
b = float(input(f"{azul}Digite o valor de Y: {reset}"))
c = float(input(f"{azul}Digite o valor de Z: {reset}"))
d = float(input(f"{azul}Qual é o resultado da equação?\n{reset}"))
e = float(input(f"{azul}Digite o valor de X: {reset}"))
f = float(input(f"{azul}Digite o valor de Y: {reset}"))
g = float(input(f"{azul}Digite o valor de Z: {reset}"))
h = float(input(f"{azul}Qual é o resultado da equação?\n{reset}"))
i = float(input(f"{azul}Digite o valor de X: {reset}"))
j = float(input(f"{azul}Digite o valor de Y: {reset}"))
k = float(input(f"{azul}Digite o valor de Z: {reset}"))
l = float(input(f"{azul}Qual é o resultado da equação?\n{reset}"))

# CALCULANDO O DETERMINANTE INICIAL
# MULTIPLICANDO AS DIAGONAIS
# LADO DIREITO
afk = a * f * k
bgi = b * g * i
cej = c * e * j

# LADO ESQUERDO
ifc = i * f * c
jga = j * g * a
keb = k * e * b

# SOMATORIA DOS RESULTADOS MULTIPLICADOS
# LADO DIREITO
soma1 = afk + bgi + cej

# LADO ESQUERDO
soma2 = ifc + jga + keb

# SUBTRAÇÃO DOS RESULTADOS SOMADOS / DIREITO - ESQUERDO
det_inicial = soma1 - soma2

# CALCULANDO O DETERMINANTE DE  X
# MULTIPLICANDO AS DIAGONAIS
# LADO DIREITO
dfk = d * f * k
bgl = b * g * l
chj = c * h * j

# LADO ESQUERDO
lfc = l * f * c
jgd = j * g * d
khb = k * h * b

# SOMATORIA DOS RESULTADOS MULTIPLICADOS
# LADO DIREITO
soma_x = dfk + bgl + chj

# LADO ESQUERDO
soma_x1 = lfc + jgd + khb

# SUBTRAÇÃO DOS RESULTADOS SOMADOS / DIREITO - ESQUERDO
det_x = soma_x - soma_x1

# CALCULANDO O DETERMINANTE DE  Y
# MULTIPLICANDO AS DIAGONAIS
# LADO DIREITO
ahk = a * h * k
dgi = d * g * i
cel = c * e * l

# LADO ESQUERDO
ihc = i * h * c
lga = l * g * a
ked = k * e * d

# SOMATORIA DOS RESULTADOS MULTIPLICADOS
# LADO DIREITO
soma_y = ahk + dgi + cel

# LADO ESQUERDO
soma_y1 = ihc + lga + ked

# SUBTRAÇÃO DOS RESULTADOS SOMADOS / DIREITO - ESQUERDO
det_y = soma_y - soma_y1

# CALCULANDO O DETERMINANTE DE  Z
# MULTIPLICANDO AS DIAGONAIS
# LADO DIREITO
afl = a * f * l
bhi = b * h * i
dej = d * e * j

# LADO ESQUERDO
ifd = i * f * d
jha = j * h * a
leb = l * e * b

# SOMATORIA DOS RESULTADOS MULTIPLICADOS
# LADO DIREITO
soma_z = afl + bhi + dej

# LADO ESQUERDO
soma_z1 = ifd + jha + leb

# SUBTRAÇÃO DOS RESULTADOS SOMADOS / DIREITO - ESQUERDO
det_z = soma_z - soma_z1

# DIVISÃO DOS DET DE X, Y, e Z POR DET INICIAL
# condição
if det_inicial == 0:
    print(" ")
    print(f"{laranja}Não é possível dividir por 0!{reset}")
    print(" ")
    sleep(2)
    print(f"{laranja}Tente outro valor!{reset}")
    print(" ")
    sleep(2)
    print(f"{azul}Grupo: Jéssica De Jesus Da Silva {reset}")
    sleep(1)
    print(f"{azul}       Tamires Dionizia De Jesus Benardes {reset}")
    sleep(1)
    print(f"{azul}       Lavínia De Souza Freitas {reset}")
    sleep(1)
    print(f"{azul}       Marina Romera Amorim {reset}")
    sleep(1)
    print(f"{azul}       Riani Katelin Da Silva {reset}")
    print(" ")
    sleep(1)
    input(f"{laranja}Para sair aperte 'Enter'{reset}")

# RESULTADO DE X
valor_x = det_x / det_inicial

# RESULTADO DE Y
valor_y = det_y / det_inicial

# RESULTADO DE Z
valor_z = det_z / det_inicial

print(" ")
print(f"{laranja}Calculando....{reset}")
print(" ")
sleep(3)

# EXIBINDO O RESULTADO FINAL
print(f"{verde}X = {valor_x}{reset}")
print(f"{verde}Y = {valor_y}{reset}")
print(f"{verde}Z = {valor_z}{reset}")
print(" ")
sleep(2)
print(f"{laranja}Participantes do Grupo: {reset}")
sleep(1)
print(f"{azul}Jéssica de Jesus Da Silva --> RA: 3023200546{reset}")
sleep(1)
print(f"{azul}Tamires Dionizia De Jesus Bernardes --> RA: 3023200548{reset}")
sleep(1)
print(f"{azul}Lavínia De Souza Freitas --> RA: 3023202645{reset}")
sleep(1)
print(f"{azul}Marina Romera Amorim --> RA: 3023108400{reset}")
sleep(1)
print(f"{azul}Riani Katelin Da Silva {reset}")
print(" ")
sleep(1)
input(f"{laranja}Para sair aperte 'Enter'{reset}")
print(" ")
