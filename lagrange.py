# MÉTODO DE LAGRANGE - INTERPOLAÇÃO POLINOMIAL

# DESCRIÇÃO PARA O USUÁRIO

print(" ")
print("Projeto em Sistemas Inteligentes")
print(" ")
print("Direção: Prof° Sergio João Guimaraes Da Silva")
print(" ")
print("Método de Lagrange Interpolação Polinomial")
print(" ")

# ENTRADA PARA OS USUÁRIOS

a = float(input("Digite o valor de X: "))     #X0   
b = float(input("Digite o valor de X: "))     #X1
c = float(input("Digite o valor de X: "))     #X2
d = float(input("Digite o valor de f(x): "))  #Fx0
e = float(input("Digite o valor de f(x): "))  #Fx1
f = float(input("Digite o valor de f(x): "))  #Fx2

# CONSTANTE

x = 1

# MULTIPLICAÇÃO DAS VARIÁVEIS DE ENTRADA L0

# L0 = (X-X1).(X-X2) = (x-b).(x-c)
#      (X0-X1).(X0-X2) = (a-b).(a-c)

# PARTE DE CIMA

xx = x * x
xc = x * (-c)
bx = (-b) * x
bc = (-b) * (-c)
 
# PARTE DE BAIXO

aa = a * a
ac = a * (-c)
ba = (-b) * a 
bcb = (-b) * (-c)

# SOMA - PARTE DE BAIXO - L0

sl0b = aa + ac + ba + bcb

# MULTIPLICAÇÃO DAS VARIÁVEIS DE ENTRADA L1

# L1 = (X-X0).(X-X2) = (x-a).(x-c)
#      (X1-X0).(X1-X2) = (b-a).(b-c)

# PARTE DE CIMA

xx1 = x * x
xc1 = x * (-c)
ax1 = (-a) * x
ac1 = (-a) * (-c)

# PARTE DE BAIXO.

bb1 = b * b
bc1 = b * (-c)
ab1 = (-a) * b 
ac1b = (-a) * (-c)

# SOMA - PARTE DE BAIXO - L1

sl1b = bb1 + bc1 + ab1 + ac1b

# MULTIPLICAÇÃO DAS VARIÁVEIS DE ENTRADA L2

# L2 = (X-X0).(X-X1) = (X-a).(X-b)
#      (X2-X0).(X2-X1) = (c-a).(c-b)

# PARTE DE CIMA

xx2 = x * x
xb2 = x * (-b)
ax2 = (-a) * x
ab2 = (-a) * (-b)

# PARTE DE BAIXO

cc2 = c * c
cb2 = c * (-b)
ac2 = (-a) * c 
ab2b = (-a) * (-b)

# SOMA - PARTE DE BAIXO - L2

sl2b = cc2 + cb2 + ac2 + ab2b

# MULTIPLICAÇÃO DE f(x0)*L0 + f(x1)*L1 + f(x2)*L2

# f(x0)*L0

dx = d * xx
dxc = d * xc
dbx = d * bx
dbcb = d * bcb

# f(x1)*L1

ex = e * xx1
exc1 = e * xc1
eax1 = e * ax1
eac1 = e  * ac1b

# f(x2)*L2

fx = f * xx2
fxb2 = f * xb2
fax2 = f * ax2
fab2 = f * ab2b
  
# CALCULANDO O MMC DE L0 L1 e l2

mmc = max(sl0b, sl1b, sl2b)
while mmc % sl0b != 0 or mmc % sl1b != 0 or mmc % sl2b != 0:
  mmc += 1

# CONDIÇÃO CASO DER 0


if sl0b and sl1b and sl2b == 0:
  print(" ")
  print("Impossível dividir por 0!")
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

# SOMATORIA DE L0 L1 e L2 DIVIDIDO POR MMC

# L0
mmcl0 = mmc / sl0b

# L1
mmcl1 = mmc / sl1b

# L2
mmcl2 = mmc / sl2b

# MULTPLICÇÃO DO RESULTADO DA DIVISÃO PELAS VARIÁVEIS DE CIMA
    
# L0

l0m0 = dx * mmcl0
l0m1 = dxc * mmcl0
l0m2 = dbx * mmcl0
l0m3 = dbcb * mmcl0

# SOMA DAS VARIÁVEIS DO MEIO DO L1

l0m0_soma = l0m1 + l0m2

# L1

l1m0 = ex * mmcl1
l1m1 = exc1 * mmcl1
l1m2 = eax1 * mmcl1
l1m3 = eac1 * mmcl1

# SOMA DAS VARIÁVEIS DO MEIO DO L1

l1m1_soma = l1m1 + l1m2

# L2

l2m0 = fx * mmcl2
l2m1 = fxb2 * mmcl2
l2m2 = fax2 * mmcl2
l2m3 = fab2 * mmcl2

# SOMA DAS VARIÁVEIS DO MEIO DO L2

l2m0_soma = l2m1 + l2m2

# SOMANDO OS IGUAIS

soma_xr = l0m0 + l1m0 + l2m0
soma_meior = l0m0_soma + l1m1_soma + l2m0_soma
soma_fimr = l0m3 + l1m3 + l2m3

# MUDANDO AS VARIÁVEIS FLOAT PARA O TIPO STRING

soma_x = str(soma_xr)
soma_meio = str(soma_meior)
soma_fim = str(soma_fimr)

# EXIBINDO O RESULTADO FINAL DA INTERPOLAÇÃO

print(" ")
print("Calculando.... ")
print(" ")

print(f"         {soma_x}x² {soma_meio}x + {soma_fim}")
print(f"P2(x) = -----------------------")
print(f"                {mmc}")
print("_" * 75)
print("Grupo: Jéssica de Jesus Da Silva ")
print("       Tamires Dionizia De Jesus Benardes ")
print("       Lavínia De Souza Freitas ")
print("       Marina Romera Amorim ")
print("       Riani Katelin Da Silva ")
print(" ")
input("Para sair aperte 'Enter'")
print(" ")
