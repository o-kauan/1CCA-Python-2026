notaA = float(input("Digite a 1ª nota: "))
while notaA > 10 or notaA < 0:
    print("MELHORE")
    notaA = float(input("Digite a 1ª nota novamente: "))

notaB = float(input("Digite a 2ª nota: "))
while notaB > 10 or notaB < 0:
    print("MELHORE mais")
    notaB = float(input("Digite a 2ª nota novamente: "))


media = (notaA + notaB) / 2
print("média: ", media)