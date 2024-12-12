import re 
import sys


# Cálculo primeiro digito 
entrada = input("Digite seu cpf: ")
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)
entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print("Você enviou dados sequenciais!")
    sys.exit()

nove_digitos = cpf_enviado_usuario[:9]
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

dez_digitos = cpf_enviado_usuario[:10]
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


if cpf_enviado_usuario == cpf_gerado:
    print("O cpf é válido!")
else:
    print("O cpf é inválido!")
