import random
namen = []

while True:
    naam = input('Geef een naam: ')
    if naam in namen:
        print(f'De naam {naam} is al in de lijst!')
    else:
        namen.append(naam)
    if len(namen) >= 3:
        naam = input("Wil je nog een naam invoeren (I) of lootjes trekken (L)? ").upper()
        if naam == 'L':
            break

nuw_list = namen.copy()
random.shuffle(nuw_list)

for i in range(len(namen)):
    while nuw_list[i] == namen[i]:
        random.shuffle(nuw_list)
    if nuw_list[i] != namen[i]:
        print(f"{namen[i]} trekt {nuw_list[i]}")


 