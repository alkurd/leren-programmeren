def NameAndAge():
    name = input('Wat is je naam: \n')
    age = int(input('Wat is je leeftijd: \n'))
    library = {'name': name, 'age': age}
    return library



def getMultipleNamesAndAges():
    lijst = []
    while True:
        naam = NameAndAge()
        lijst.append(naam)
        NieuwNaam = input('wil je nog een naam toevoegen?' ).lower()
        if NieuwNaam != 'ja':
            break
    return lijst


people = getMultipleNamesAndAges()

for person in people:
    print(f"{person['name']} is {person['age']} jaar")