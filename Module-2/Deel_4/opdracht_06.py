from fruitmand import fruitmand

gebruiker = input("Please select een fruit: ")#<<<<<------- nieuw toe gevoegd
for fruit in fruitmand:
    if fruit['name'] == gebruiker:
        print(fruit['weight'])