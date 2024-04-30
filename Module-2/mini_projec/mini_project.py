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

dict_list = {} 

while True:
    gevonden =  False
    for i in range (len(namen)):
        if nuw_list[i] == namen[i]:
            gevonden = True
            random.shuffle(nuw_list)

            break
    if not gevonden:
        for i in range (len(namen)):
            dict_list[namen[i]] = nuw_list[i]
        break

while True:
    naam_opvraag =  input('vraag een naam op ')
    if naam_opvraag not in dict_list:
        print(f'{naam_opvraag} was niet toe gevonden')
    elif naam_opvraag  in dict_list:
        print(f'{naam_opvraag} trekt {dict_list[naam_opvraag]}')
    if naam_opvraag == 'q':
        break

# if naam_opvraag in dict_list:
#         print(f'{naam_opvraag} trekt {dict_list[naam_opvraag]}')
#     else:
#         print(f'{naam_opvraag} was niet toe gevonden')
    

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