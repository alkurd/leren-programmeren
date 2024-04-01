PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30
over_21_and_VIP = {
'BLAUWE_BANDJE' : False,
'ROODE_BANDJE' : False,
"STAMPELL" : False}
DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi','yousef')

#bouw hieronder de floowchart na
print('je loopt een clup binnen')
print('je aan de voor duur word je gestopt door security')
age = int(input('hij vraagt hoe oud ben je?\n'))
if age < 18 :
    print('mindere jaregen mogen de clup niet binnen komen')
    exit()
else:
    name = input('wat is je naam?\n')
    if name in VIP_LIST:
        print(f'je bent in de VIP seat van {name}')
        if age >= 21:
            over_21_and_VIP['BLAUWE_BANDJE'] = True
            print ('u krijgt een blauwe bandje')
        else:
            over_21_and_VIP['ROODE_BANDJE'] = True
            print ('u krijgt een roode bandje')
    else:
        print(f'je bent niet in de VIP seat menier {name}')
        if age >= 21:
            over_21_and_VIP['STAMPELL'] = True
            print ('u krijgt een stampell')
    drinks = input('wat wil je drinken?\n')
    if drinks not in DRANKJES:
        print ('ik weet niet wat je bedoelt,hier een glasje water!')
        exit()
    else:
        complimenten = 'hier complimenten van het huis'
        if drinks == 'cola':
            if  any (over_21_and_VIP.values()):
                print (complimenten)
            else:
                print(f'altublief je {drinks}, de prijst is {PRIJS_COLA} euro ')
        elif drinks == 'bier':
            if age >= 21 and  over_21_and_VIP['BLAUWE_BANDJE']:
                print (complimenten)
            elif age >= 21 and over_21_and_VIP['STAMPELL']:
                print(f'altublief je {drinks}, de prijst is {PRIJS_BIER} euro ')
            else:
                print('sorry mag geen alcoholn bestellen onder de 21')
                exit()
        elif drinks == 'champagne':
            if over_21_and_VIP ['BLAUWE_BANDJE'] == True:
                print(f'altublief je {drinks}, de prijst is {PRIJS_CHAMPAGNE} euro ')
            else:
                print(f'Sorry allen VIP`s ouder dan 21 mogen {drinks} bestellen')
                exit()