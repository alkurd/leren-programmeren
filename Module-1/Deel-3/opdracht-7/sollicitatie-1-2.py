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
Min_gewicht = 90
Max_gewicht = 120
praktijkervaring_met_dieren_dressuur = 4
ervaring_met_jongleren = 5
ervaring_met_acrobatiek = 5

#statment
naam=input('wat is u naam ? ').lower()
geslacht=input('wat is u geslacht ? ').lower()
if geslacht == 'man':
    man = input('Heeft u een snor? (Ja/Nee)').lower()
elif geslacht == 'vrouw':
    vrouw = input('Heeft u rood krulhaar? (Ja/Nee)').lower()
elif geslacht =='zeg ik liever niet':
    zeg_ik_liever_niet= input('heeft u een brede glimlach').lower()
else:
   glimlag= input('heeft u een brede glimlach? ').lower()

vrachtwagenrijbewijs = input('Bent u in het bezit van een vrachtwagenrijbewijs? (Ja/Nee)').lower()
hoge_hoed = input('Heeft u een hoge hoed? (Ja/Nee)').lower()
lengte = int(input('Hoe lang bent u in centimeters? '))
gewicht = int(input('Hoeveel weegt u in kilogram? '))
praktijkervaring_met_dieren_dressuur1 = int(input('Hoeveel jaren heeft u ervaring met dieren dressuur? '))
ervaring_met_jongleren1 = int(input('Hoeveel jaren heeft u ervaring met jongleren? '))
ervaring_met_acrobatiek1= int(input('Hoeveel jaren heeft u ervaring met acrobatiek? '))

geschikt = (
    # geslacht== man or geslacht== vrouw or geslacht== zeg_ik_liever_niet and
    vrachtwagenrijbewijs=='ja' and hoge_hoed=='ja' and
    Min_gewicht <= gewicht <= Max_gewicht and(
    praktijkervaring_met_dieren_dressuur1 >= praktijkervaring_met_dieren_dressuur or
    ervaring_met_jongleren1 >= ervaring_met_jongleren or
    ervaring_met_acrobatiek1 >= ervaring_met_acrobatiek
    )
)

if geschikt:
    print(f'Beste {naam},')
    print('Gefeliciteerd! U mag solliciteren naar de functie van Circusdirecteur bij Circus HotelDeBotel.')
else:

    print(f'Beste {naam},')
    print('Helaas, u voldoet niet aan alle criteria voor deze functie')
    if 'man' in locals() and man == 'nee':
        print('u heeft geen snor')
    if 'vrouw' in locals() and vrouw =='nee':
        print ('u heeft geen rood krulhaar')
    if 'zeg_ik_liever_niet' in locals () and zeg_ik_liever_niet == 'nee':
        print ('u heeft geen brede glimlach')
    if 'glimlag' in locals () and glimlag == 'nee':
        print ('u heeft geen brede glimlach')
    if vrachtwagenrijbewijs=='nee':
        print('u heeft geen vrachtwagenrijbewijs ')
    if hoge_hoed=='nee':
        print('u heeft geen hoge hoed')
    if gewicht < Min_gewicht:
        print('U bent te licht.')
    if gewicht > Max_gewicht:
        print('U bent te zwaar.')
    if praktijkervaring_met_dieren_dressuur1 < praktijkervaring_met_dieren_dressuur:
        print('U heeft niet genoeg ervaring met dieren dressuur.')
    elif ervaring_met_jongleren1 < ervaring_met_jongleren:
        print('U heeft niet genoeg ervaring met jongleren.')
    elif ervaring_met_acrobatiek1 < ervaring_met_acrobatiek:
        print('U heeft niet genoeg ervaring met acrobatiek.')
