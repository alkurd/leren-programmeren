from fruitmand import fruitmand
num =0
for i in fruitmand:
    num += 1
    print(f"{num}. {i['name']}: {i['weight']}: {i['color']}: {i['round']}")