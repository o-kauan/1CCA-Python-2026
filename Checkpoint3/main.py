# Kauan Damasceno de Lima - RM: 573727
# Thiago Soalheiro Diamantino - RM: 569316

temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]
lista = []
for turma in range(len(temperaturas)):
    print("Salas:", turma+1)
    print("Média:", sum(temperaturas[turma])/(len(temperaturas[turma])))
    i = 0
    for grau in (temperaturas[turma]):
        if grau >= 33:
            i = 1 + i
    lista.append(i)
    print("Registros crítcos:", i)
    print()
print("Sala com maior risco: Sala ", lista.index((max(lista))) + 1)



