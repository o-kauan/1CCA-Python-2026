t = ('a','b','c','d')
print(t[1:]) # começa a mostrar a partir do segundo

t1 = 'A'
t2 = t1
print(t2)

# ATRIBUIÇÃO DE TUPLAS
a = 5
b = 10

a,b = b,a
print(a,b)

email = "fulano@gmail.com"
username, domain = email.split("@")
print(username)
print(domain)
