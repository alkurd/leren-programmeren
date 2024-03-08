NUMBER = 50
doelNumber = 0
nextNuber = 50
volgend_getal = 50  # Start vanaf 50 in plaats van 0
alles = []

while doelNumber <= 1000:
    volgend_getal += 1  # Verhoog volgend_getal bij elke iteratie
    vorigeWaarde = nextNuber  # Sla de vorige waarde van nextNuber op
    nextNuber += volgend_getal  # Voeg volgend_getal toe aan nextNuber voor de cumulatieve som
   
    print(f'{NUMBER} + {vorigeWaarde} = {nextNuber}')
    doelNumber = nextNuber
    # nextNuber += 1
    
    
    # if nextNuber >= 1000:
        
    #     break




   







# def points(matches):
#     total_points = 0
#     for match in matches:
#         x, y = map(int, match.split(":"))
#         if x > y:
#             total_points += 3
#         elif x == y:
#             total_points += 1
#     return total_points


# matches = ["3:1", "2:2", "0:1", "4:0", "1:2", "2:1", "3:3", "1:0", "0:4", "2:0"]
# print("Total points:", points(matches))