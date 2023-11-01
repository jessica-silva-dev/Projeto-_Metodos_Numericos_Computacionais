# MÉTODO DE CRAMER

# DESCRIÇÃO PARA O USUÁRIO

print(" ")
print("Projeto em Sistemas Inteligentes")
print(" ")
print("Direção: Prof° Sergio João Guimaraes Da Silva")
print(" ")
print("Método de Cramer")
print(" ")

# ENTRADA DE DADOS DO USUÁRIO

a = float(input('Digite o valor de X: '))
b = float(input('Digite o valor de Y: '))
c = float(input('Digite o valor de Z: '))
d = float(input('é =  '))
e = float(input('Digite o valor de X: '))
f = float(input('Digite o valor de Y: '))
g = float(input('Digite o valor de Z: '))
h = float(input('é =  '))
i = float(input('Digite o valor de X: '))
j = float(input('Digite o valor de Y: '))
k = float(input('Digite o valor de Z: '))
l = float(input('é =  '))

# DEMONSTRAÇÃO

''' 
  VARIÁVEIS     DET INICIAL
  X Y Z
                              
  a b c = d     a b c a b 
  e f g = h     e f g e f
  i j k = l     i j k i j   
'''
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

# DEMONSTRAÇÃO

''' 
  VARIÁVEIS     DET X
  X Y Z
                              
  a b c = d     d b c d b 
  e f g = h     h f g h f
  i j k = l     l j k l j   
'''
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

# DEMONSTRAÇÃO

''' 
  VARIÁVEIS     DET Y
  X Y Z
                              
  a b c = d     a d c a d 
  e f g = h     e h g e h
  i j k = l     i l k i l   
'''
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

# DEMONSTRAÇÃO

''' 
  VARIÁVEIS     DET Z
  X Y Z
                              
  a b c = d     a b d a b 
  e f g = h     e f h e f
  i j k = l     i j l i j   
'''
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
  print("Não é possível dividir por 0!")
  print(" ")
  print("Tente outro valor!")
  print(" ")
  print("Grupo: Jéssica De Jesus Da Silva ")
  print("       Tamires Dionizia De Jesus Benardes ")
  print("       Lavínia De Souza Freitas ")
  print("       Marina Romera Amorim ")
  print("       Riani Katelin Da Silva ")
  print(" ")
  input("Para sair aperte 'Enter'")


# RESULTADO DE X

valor_x = det_x / det_inicial

# RESULTADO DE Y

valor_y = det_y / det_inicial

# RESULTADO DE Z

valor_z = det_z / det_inicial

print(" ")
print("Calculando....")
print(" ")
print(f'X =', valor_x)
print(f'Y =', valor_y)
print(f'Z =', valor_z)
print(" ")
print("Grupo: Jéssica de Jesus Da Silva ")
print("       Tamires Dionizia De Jesus Benardes ")
print("       Lavínia De Souza Freitas ")
print("       Marina Romera Amorim ")
print("       Riani Katelin Da Silva ")
print(" ")
input("Para sair aperte 'Enter'")
print(" ")
