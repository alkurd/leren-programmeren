from fruitmand import fruitmand

for fruit in fruitmand:
    if not fruit['round']:
        print(f'{fruit['name']} is rond')