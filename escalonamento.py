# ESCALONAMENTO

# ESTRADA DE DADOS DO USUÁRIO

a = int(input('Digite o valor de X: '))
b = int(input('Digite o valor de Y: '))
c = int(input('Digite o valor de Z: '))
d = int(input('é =  '))
e = int(input('Digite o valor de X: '))
f = int(input('Digite o valor de Y: '))
g = int(input('Digite o valor de Z: '))
h = int(input('é =  '))
i = int(input('Digite o valor de X: '))
j = int(input('Digite o valor de Y: '))
k = int(input('Digite o valor de Z: '))
l = int(input('é =  '))

# DEMONSTRAÇÃO

''' 
  VARIÁVEIS     DET INICIAL
  X Y Z
                              
  a b c = d     a b c a b 
  e f g = h     e f g e f
  i j k = l     i j k i j   
'''
# CALCULANDO O DETERMINANTE INICIAL

# Multiplicando as diagonais

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

#SUBTRAÇÃO DOS RESULTADOS SOMADOS / DIREITO - ESQUERDO

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

# Multiplicando as diagonais

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

#SUBTRAÇÃO DOS RESULTADOS SOMADOS / DIREITO - ESQUERDO

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

# Multiplicando as diagonais

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

#SUBTRAÇÃO DOS RESULTADOS SOMADOS / DIREITO - ESQUERDO

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

# Multiplicando as diagonais

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

#SUBTRAÇÃO DOS RESULTADOS SOMADOS / DIREITO - ESQUERDO

det_z = soma_z - soma_z1

# DIVISÃO DOS DET DE X, Y, e Z POR DET INICIAL

# RESULTADO DE X

valor_x = det_x / det_inicial

# RESULTADO DE Y

valor_y = det_y / det_inicial

# RESULTADO DE Z

valor_z = det_z / det_inicial

#FAZENDO O ESCALONAMENTO

''' 
DEMOSTRAÇÃO DA EQUAÇÃO

  VARIÁVEIS 
    
  X Y Z
                              
  a b c = d     
  e f g = h    
  i j k = l    
      
'''

# RESULTADO ESCALONAMENTO DE Z

esc_z = valor_z / k

# RESULTADO ESCALONAMENTO DE Y

esc_y1 = f + g 
esc_y2 = esc_y1 * esc_z
esc_y = esc_y2 + valor_y

# RESULTADO ESCALONAMENTO DE X

esc_x1 = a + b
esc_x2 = esc_x1 * esc_y
esc_x3 = (esc_x2 + c) * esc_z
esc_x = esc_x3 + valor_x

# IMPRIMIR PARA O USUÁRIO

print(f'X =', esc_x)
print(f'Y =', esc_y)
print(f'Z =', esc_z)
