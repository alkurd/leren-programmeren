
dagen_van_de_week = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")
# print("Alle dagen van de week zijn:", ", ".join(dagen_van_de_week))
# werkdagen = dagen_van_de_week[:5]
# print("De werkdagen zijn:", ", ".join(werkdagen))
# weekenddagen = dagen_van_de_week[-2:]
# print("De weekenddagen zijn:", ", ".join(weekenddagen))
# print("Alle dagen van de week in omgekeerde volgorde zijn:", ", ".join(reversed(dagen_van_de_week)))
# print("De werkdagen in omgekeerde volgorde zijn:", ", ".join(reversed(werkdagen)))
# print("De weekenddagen in omgekeerde volgorde zijn:", ", ".join(reversed(weekenddagen)))

print("Alle dagen van de week zijn: ",end= '')
for dag in dagen_van_de_week:
    print(dag, end=', ')
print()

werkdagen = dagen_van_de_week [:5]
print('alle werk dagen zijn: ', end='')
for dag in werkdagen:
    print(dag, end=', ')
print()

weekeddagen = dagen_van_de_week [-2:]
print('Alle weekenddagen zijn: ', end='')
for dag in weekeddagen:
    print(dag, end=', ')
print()

print('Alle weekeddagen om gekeerd zijn: ', end = '')
for dag in reversed (dagen_van_de_week):
    print(dag, end= ', ')
print()

werkdagen = dagen_van_de_week [:5]
print('alle werk dagen om gekeerd zijn: ', end='')
for dag in reversed(werkdagen):
    print(dag, end=', ')
print()

weekeddagen = dagen_van_de_week [-2:]
print('Alle weekenddagen om gekeerd zijn: ', end='')
for dag in reversed(weekeddagen):
    print(dag, end=', ')
print()