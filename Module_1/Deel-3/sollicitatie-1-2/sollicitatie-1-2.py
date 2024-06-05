# aankondiging tekst
print("+" * 37)
print('+{:^35}+'.format('Sollicitatieformulier'))
print("+" * 37)
print('Er worden u een aantal relevante vragen gesteld...')
print('Gelieve deze naar eer en geweten in te vullen.')
print('Als blijkt dat u aan de criteria voldoet, komt u in')
print('aanmerking voor een serieus sollicitatiegesprek!')
print('Ontspan maar blijf alert, hier komen de vragen')

# variabelen
Min_gewicht = 60
Max_gewicht = 120
praktijkervaring_met_dieren_dressuur = 4
ervaring_met_jongleren = 5
ervaring_met_acrobatiek = 5
snor = ''
roodhaar = ''
glimlach = ''

#statment
naam=input('wat is u naam ? ').lower()
geslacht=input('wat is u geslacht ? ').lower()
if geslacht == 'man':
    snor = input('Heeft u een snor? (Ja/Nee)').lower()=='ja'
elif geslacht == 'vrouw':
    roodhaar = input('Heeft u rood krulhaar? (Ja/Nee)').lower()=='ja'
elif geslacht =='zeg ik liever niet':
    glimlach= input('heeft u een brede glimlach').lower()=='ja'

vrachtwagenrijbewijs = input('Bent u in het bezit van een vrachtwagenrijbewijs? (Ja/Nee)').lower()=='ja'
hoge_hoed = input('Heeft u een hoge hoed? (Ja/Nee)').lower()=='ja'
lengte = int(input('Hoe lang bent u in centimeters? '))>=150
gewicht = int(input('Hoeveel weegt u in kilogram? '))
gewicht <= Min_gewicht or gewicht >= Max_gewicht
praktijkervaring_met_dieren_dressuur = int(input('Hoeveel jaren heeft u ervaring met dieren dressuur? '))>=praktijkervaring_met_dieren_dressuur
ervaring_met_jongleren = int(input('Hoeveel jaren heeft u ervaring met jongleren? '))>=ervaring_met_jongleren
ervaring_met_acrobatiek= int(input('Hoeveel jaren heeft u ervaring met acrobatiek? '))>=ervaring_met_acrobatiek

geschikt = ((snor or roodhaar or glimlach) and
    vrachtwagenrijbewijs and hoge_hoed and
   gewicht and(
    praktijkervaring_met_dieren_dressuur or
    ervaring_met_jongleren or
    ervaring_met_acrobatiek 
    )
)

if geschikt:
    print(f'Beste {naam},')
    print('Gefeliciteerd! U mag solliciteren naar de functie van Circusdirecteur bij Circus HotelDeBotel.')
else:

    print(f'Beste {naam},')
    print('Helaas, u voldoet niet aan alle criteria voor deze functie')
    if snor == 'nee':
        print('u heeft geen snor')
    if roodhaar =='nee':
        print ('u heeft geen rood krulhaar')
    if glimlach == 'nee':
        print ('u heeft geen brede glimlach')
    if vrachtwagenrijbewijs=='nee':
        print('u heeft geen vrachtwagenrijbewijs ')
    if hoge_hoed=='nee':
        print('u heeft geen hoge hoed')
    if gewicht < Min_gewicht:
        print('U bent te licht.')
    if gewicht > Max_gewicht:
        print('U bent te zwaar.')
    if praktijkervaring_met_dieren_dressuur < praktijkervaring_met_dieren_dressuur:
        print('U heeft niet genoeg ervaring met dieren dressuur.')
    elif ervaring_met_jongleren < ervaring_met_jongleren:
        print('U heeft niet genoeg ervaring met jongleren.')
    elif ervaring_met_acrobatiek < ervaring_met_acrobatiek:
        print('U heeft niet genoeg ervaring met acrobatiek.')
