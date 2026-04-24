def verificar_nota(nota):
    while nota > 10 or nota < 0:
        print("erro 404")
        nota = float(input(f"Digite a nota novamente: "))
    return nota

notaA = float(input("Digite a 1ª nota: "))
notaA = verificar_nota(notaA)

notaB = float(input("Digite a 2ª nota: "))
notaB = verificar_nota(notaB)

media = (notaA + notaB) / 2
print("média: ", media)