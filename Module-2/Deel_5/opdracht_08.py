from fruitmand import fruitmand
watermaloen = {'weight' : 100}
fruitmand.append(watermaloen)
totaal = 0
for waarde in fruitmand:
    totaal += waarde['weight']
print(totaal)