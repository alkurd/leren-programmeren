from fruitmand import fruitmand
watermaloen = {
    'name' : 'watermaloen',
    'weight' : 100,
    'color' : 'green',
    'round' : True}
fruitmand.append(watermaloen)
totaal = 0
for waarde in fruitmand:
    totaal += waarde['weight']
print(totaal)