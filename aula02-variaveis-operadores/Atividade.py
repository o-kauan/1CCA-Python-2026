# DESAFIO 1
nome = input("Qual é o seu nome: ")
k = int(input("Selecione a mensagem de boas vindas (1, 2 ou 3): "))

if k == 1:
    print(f"Bom dia {nome}")
if k == 2:
    print(f"Boa tarde {nome}")
if k == 3:
    print(f"Boa noite {nome}")
else:
    print(f"Catapimbas você não sabe escolher um número entre 1 e 3")

# DESAFIO 2
dia = 21
ano = 2007
mes = 11

print(f"{dia}/{mes}/{ano}")
