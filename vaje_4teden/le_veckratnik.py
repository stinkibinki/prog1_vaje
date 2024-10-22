xs = [5, 4, -7, 42, 12, -3, -4, 11, 42, 2]
veckratnik = True
for x in xs:
    if x % 42 != 0:
        veckratnik = False

print(veckratnik)