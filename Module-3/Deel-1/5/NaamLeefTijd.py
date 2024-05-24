def NameAndAge():
    name = input('Wat is je naam: \n')
    woonplaats = input('welke stad woon je: \n')
    age = int(input('Wat is je leeftijd: \n'))
    library = {'name': name,'woonplaats':woonplaats, 'age': age}
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
if __name__ == '__main__':

    people = getMultipleNamesAndAges()

    for person in people:
        print(f"{person['name']} die in {person['woonplaats']} woont is {person['age']} jaar")