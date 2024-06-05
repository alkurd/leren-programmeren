from fruitmand import fruitmand
kleuren = []
# for fruit in fruitmand:

for fruit in fruitmand:
    if fruit['name'] != 'druif':
        if fruit['color'] not in kleuren:
            kleuren.append(fruit['color'])
    
print(kleuren)
