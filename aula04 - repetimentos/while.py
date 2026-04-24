cp = 0
i = 0

while i < 10:
    i += 1

    if i == 3 or i == 5:
        continue # pula e continua

    if i == 8:
        break # para antes

    print("produto:", i)


