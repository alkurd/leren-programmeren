#opdracht 8
from NaamLeefTijd import getMultipleNamesAndAges

people = getMultipleNamesAndAges()

for person in people:
    print(f"{person['name']} die in {person['woonplaats']} woont is {person['age']} jaar")
#eind opdracht 8