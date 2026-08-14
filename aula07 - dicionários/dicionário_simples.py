eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {
    'one': 'uno',
    'two': 'dos',
    'four': 'quatro',
    'five': 'cinco'
}

print(eng2sp)
print(eng2sp['two'])

print('tree' in eng2sp)

print()

for i in eng2sp:
    print (i)

print ('-' * 10)

for i in eng2sp:
    print (eng2sp[i])


def cont_letter (s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

print(cont_letter('BATATA'))