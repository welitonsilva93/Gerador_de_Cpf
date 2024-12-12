import random


nove_digitos = ''

for a in range(9):
    nove_digitos += str(random.randint(0,9))


cpf_numero = [int(digito) for digito in nove_digitos]

sequencia = [10,9,8,7,6,5,4,3,2]
resultado_final = []

for digito, seq in zip(cpf_numero, sequencia):
    resultado = digito * seq
    resultado_final.append(resultado)

soma = sum(resultado_final)
multi = soma * 10
resto_divisao = multi % 11

if resto_divisao > 9:
    primeiro_digito = 0
else:
    primeiro_digito = resto_divisao


# Cálculo Segundo digito

dez_digitos = f'{nove_digitos}{primeiro_digito}'
cpf_numero = [int(digito) for digito in dez_digitos]

sequencia = [11,10,9,8,7,6,5,4,3,2]
resultado_final = []

for digito, seq in zip(cpf_numero, sequencia):
    resultado = digito * seq
    resultado_final.append(resultado)

soma = sum(resultado_final)
multi = soma * 10
resto_divisao = multi % 11

if resto_divisao > 9:
    segundo_digito = 0
else:
    segundo_digito = resto_divisao

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

print(f'{cpf_gerado}')