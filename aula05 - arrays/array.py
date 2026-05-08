list_frutas = ["Maçã", "Morango", "Uva"]

# print(list_frutas[0])

for frutas in list_frutas:
    print(frutas)

list_frutas.append("Batata")
print(list_frutas[-1]) # mostra o último item da lista ?

tamanho = len(list_frutas)

for i in range(tamanho):
    print(i)

msg = "BOM DIA" # string = lista
for i in range (len(msg)):
    print(msg[i])

print()

for i in range (0, len(msg),2): # de dois em dois
    print (msg[i])


list_nomes = ['maria', 'bob', 'jose', 'caio']

i = 0
for nome in list_nomes:
    for nome2 in (list_nomes[list_nomes.index(nome) + 1: ]):
        print(nome, nome2)
        i += 1
print("quantidade de duplas possíveis:", (3+2+1), "famoso", i)

print()

for i in range (len(list_nomes)):
    for j in range (i + 1, len(list_nomes)):
        print(list_nomes[i],list_nomes[j] )