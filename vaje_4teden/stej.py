xs = [5, 4, -7, 42, 12, -3, -4, 11, 42, 2]

videl_sem_42 = False
ponovitev = 0
for x in xs:
    if x == 42:
        videl_sem_42 = True
        ponovitev += 1

print(videl_sem_42)
if videl_sem_42:
    print("Število 42 se v seznamu pojavi ", ponovitev, " krat.")