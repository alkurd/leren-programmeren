def NameAndAge():
    name = input('Wat is je naam: \n')
    age = int(input('Wat is je leeftijd: \n'))
    library = {'name': name, 'age': age}
    return library

persoon = NameAndAge()

print(f"{persoon['name']} is {persoon['age']} jaar")

