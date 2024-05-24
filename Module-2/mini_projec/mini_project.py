import random

input_namen = []
count = 0
while True:
    naam = input('Geef een naam: ')
    if naam in input_namen:
        print(f'De naam {naam} is al in de lijst!')
    else:
        if naam.lower() != 'l':
            input_namen.append(naam)

        if len(input_namen) >= 3:
            if count == 0:
                count += 1
                naam = input("Wil je nog een naam invoeren (I) of lootjes trekken (l)? ").lower()
            if naam == 'l':
                break

lootjes = input_namen.copy()
random.shuffle(lootjes)

lootjes_koppeling = {} 

while True:
    gevonden = False
    for i in range(len(input_namen)):
        if lootjes[i] == input_namen[i]:
            gevonden = True
            random.shuffle(lootjes)
            break
    if not gevonden:
        for i in range(len(input_namen)):
            lootjes_koppeling[input_namen[i]] = lootjes[i]
        break

while True:
    naam_opvraag = input('Vraag een naam op: ').lower()
    if naam_opvraag in lootjes_koppeling:
        print(f'{naam_opvraag} trekt {lootjes_koppeling[naam_opvraag]}')
    else:
        print(f'{naam_opvraag} was niet toegevoegd')
    if naam_opvraag == 'q':
        break



    

# for i in range(len(namen )):
#     print(f'{namen[i]} trekt {nuw_list[i]}') 


# while True:
#     kopie = False
#     for i in namen:
#         Gekozen_naam = random.choice(nuw_list)
#         if Gekozen_naam != i:
#             print(f'{i} trekt {Gekozen_naam}' )
#         else:
#             kopie = True
#     if kopie == False:
#         break


# for i in range(len(namen)):
#     while nuw_list[i] == namen[i]:
#         random.shuffle(nuw_list)
#     if nuw_list[i] != namen[i]:
#         gevonden = nuw_list.pop(0)
#         print(gevonden)
