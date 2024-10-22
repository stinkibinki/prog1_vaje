stevilo = int(input("Vnesite št.: "))

delitelj = stevilo
delitelji = []

while delitelj > 0:
    if stevilo % delitelj == 0:
        delitelji.append(delitelj)
    delitelj -= 1
for delitelj in delitelji:
    print(delitelj)