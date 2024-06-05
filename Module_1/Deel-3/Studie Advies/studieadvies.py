from studieadviestext import*

print(STUDIEDOKTER_TITEL)

aantal_vragen=7

vraag0=int(input(f'{AANTAL_WEKEN_VRAAG}'))

vraag1=int(input (f'{COMPETENTIE_STELLING_1}\n' f'{OPTIES}'))
vraag2=int(input (f'{COMPETENTIE_STELLING_2}\n' f'{OPTIES}'))
vraag3=int(input (f'{COMPETENTIE_STELLING_3}\n' f'{OPTIES}'))
vraag4=int(input (f'{COMPETENTIE_STELLING_4}\n' f'{OPTIES}'))
vraag5=int(input (f'{COMPETENTIE_STELLING_5}\n' f'{OPTIES}'))
if vraag0 >=10:
    vraag6=int(input (f'{COMPETENTIE_STELLING_6}\n' f'{OPTIES}'))
    vraag7=int(input (f'{COMPETENTIE_STELLING_7}\n' f'{OPTIES}'))
    conclusie=(vraag1 + vraag2 + vraag3 + vraag4 + vraag5 + vraag6 + vraag7)
    conclusie_1=(conclusie / aantal_vragen)
else:
    conclusie=(vraag1 + vraag2 + vraag3 + vraag4 + vraag5)
    conclusie_1=(conclusie / 5)

print(f'Gemiddelde score: {conclusie_1:.0f}')
if conclusie_1 <=2:
    print(COMPETENTIE_ADVIES_TITEL)
    print(COMPETENTIE_ADVIES_ZORGELIJK)
elif conclusie_1 <= 3:
    print(COMPETENTIE_ADVIES_TITEL)
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_TITEL)
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)
    