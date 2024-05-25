#opdracht 9
from NaamLeefTijd import getMultipleNamesAndAges

people = getMultipleNamesAndAges()

for person in people:
    print(f"In {person['woonplaats']} woont de {person['age']} jarige {person['name']}.")
#eind opdracht 9