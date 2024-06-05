from fruitmand import fruitmand
num = 0
for i in fruitmand:
    num += 1
    print(f"{num}. {i['name']}")

# druiven_kleuren = {}

# # De fruitmand doorlopen om de kleuren van de druiven te verzamelen
# for fruit in fruitmand:
#     if fruit['name'] == 'druif':
#         if fruit['color'] not in druiven_kleuren:
#             druiven_kleuren[fruit['color']] = fruit['name']

# # Druiven met beide kleuren printen
# for color, name in druiven_kleuren.items():
#     print(f"{name} is {color}")

# # De rest van de fruitmand printen zonder duplicaten van druiven
# for fruit in fruitmand:
#     if fruit['name'] != 'druif':
#         print(fruit)