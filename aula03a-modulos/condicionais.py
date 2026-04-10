# OPERADORES DE ATRIBUIÇÃO
num = 155
print(num)

num = num + 2
print(num)

num /= 2
print(num)

# OPERADORES RELACIONAIS

print()

idade = 20
print(idade == 20)
print(idade == 2)

maior_idade = idade >= 18
print(maior_idade)

print()
# OPERADOR LÓGICO
# LÓGICA E (and)

verifica_email = False
verifica_senha = True

login = verifica_senha and verifica_email
print(login)

if login:
    print('Entrando no programa')
else:
    print('Errou aí amigo')

print()

# NOTAS.......

nota_final = 3
if nota_final < 4:
    print('Aprovado!')
else:
    if nota_final < 6:
        print('Recuperação')
    else:
        print('Reprovado!')

print('acbaoue')