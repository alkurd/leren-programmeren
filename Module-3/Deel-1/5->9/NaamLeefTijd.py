#opdracht *5
def NameAndAge():
    library = {}
    library['name'] = input('Wat is je naam: \n')
    library['woonplaats'] = input('welke stad woon je: \n')# <-----opdracht *7
    library['age'] = int(input('Wat is je leeftijd: \n'))
    return library

# def NameAndAge():
#     name = input('Wat is je naam: \n')
    # woonplaats = input('welke stad woon je: \n')
    # age = int(input('Wat is je leeftijd: \n'))
#     library = {'name': name,'woonplaats':woonplaats, 'age': age}
#     return library

#eind opdracht *5


#opdracht *6
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
#eind opdracht *6