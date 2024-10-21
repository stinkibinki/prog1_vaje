# Novi asfalt, 15. 10. 2024

pot = int(input("Dolžina poti: "))
leto = 0

while pot > 0:
    tretjina_poti = pot // 3
    ostanek = pot % 3
    if ostanek > 0:
        tretjina_poti += 1
    pot -= tretjina_poti
    leto += 1
    print(tretjina_poti)

print(leto)
