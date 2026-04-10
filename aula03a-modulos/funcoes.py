def print_lyrics():
    print("I ain't gonna live forever")
    print("I just wanna to live while I'm alive")

print_lyrics()
print_lyrics()

print() # pular uma linha

def boas_vindas(nome):
    print(f'OLÁ, {nome}!!! BEM VINDO')
boas_vindas('Marcelo')

def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado = print(soma(10,2))
print(resultado)
print(type(resultado))