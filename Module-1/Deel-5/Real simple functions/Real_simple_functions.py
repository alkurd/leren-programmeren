from test_lib import test, report
from time import sleep
from math import pi

#opdracht A

# functies
def celinder_inhoud(diameter, hoogte):
    straal= diameter / 2
    inhoud= pi * straal ** 2 * hoogte
    return round(inhoud,1)

dimerter = 8.0
hoogte = 5.0
expact_content = 251.3
calculeted_content = celinder_inhoud (dimerter, hoogte)
naam = f'test diameter {dimerter} hogtte {hoogte}'
test(naam, expact_content,(calculeted_content))

sleep(1)

dimerter = 11.0
hoogte = 7.0
expact_content = 665.2
calculeted_content = celinder_inhoud (dimerter, hoogte)
naam = f'test diameter {dimerter} hogtte {hoogte}'
test(naam, expact_content,calculeted_content)

sleep(1)

dimerter = 18.0
hoogte = 7.0
expact_content = 1781.3
calculeted_content = celinder_inhoud (dimerter, hoogte)
naam = f'test diameter {dimerter} hogtte {hoogte}'
test(naam, expact_content,(calculeted_content))

sleep(1)

dimerter = 15.0
hoogte = 2.0
expact_content = 353.4
calculeted_content = celinder_inhoud (dimerter, hoogte)
naam = f'test diameter {dimerter} hogtte {hoogte}'
test(naam, expact_content,(calculeted_content))

sleep(1)

dimerter = 0
hoogte = 6.0
expact_content = 0.0
calculeted_content = celinder_inhoud (dimerter, hoogte)
naam = f'test diameter {dimerter} hogtte {hoogte}'
test(naam, expact_content,calculeted_content)
report()
sleep(1)

print('-' * 50)
# #opdracht B

def afrondenToStuiver(GETAL):
    STUIVER = 5
    afgerond= round(GETAL * 100 / STUIVER) * STUIVER / 100 
    # _2desimallegetaal = '{:.2f}'.format(afgerond)
    return afgerond
print(afrondenToStuiver(3.11))
sleep(1)
print(afrondenToStuiver(3.12))
sleep(1)
print(afrondenToStuiver(3.13))
sleep(1)
print(afrondenToStuiver(3.14))
sleep(1)
print(afrondenToStuiver(3.15))
sleep(1)
print(afrondenToStuiver(3.16))
sleep(1)
print(afrondenToStuiver(3.17))
sleep(1)
print(afrondenToStuiver(3.18))
sleep(1)
print(afrondenToStuiver(3.19))
sleep(1)

print('-' * 50)
#opdracht C

month_discount_brand ='Vespa, Kymoc, Yamama'.lower()
MONTH_DISCOUNT_PERCENT = 10
def calc_discount (price:float, brand:str, month_discount_brand:str)->float:
    if brand in month_discount_brand:
        discount = round(price * MONTH_DISCOUNT_PERCENT / 100 , 2 )
        return    discount 
    else:
        return 0.0
    
brand = 'vespa'
price = 500
expect= 50.0
calculeted_content = calc_discount(price, brand, month_discount_brand)
naam = f'de dicount op brand {brand} met de price {price}'
test(naam, expect, calculeted_content )
sleep(1)


brand = 'kymoc'
price = 400
expect= 40.0
calculeted_content = calc_discount(price, brand, month_discount_brand)
naam = f'de dicount op brand {brand} met de price {price}'
test(naam, expect, calculeted_content )
sleep(1)


brand = 'yamama'
price = 100
expect= 10.0
calculeted_content = calc_discount(price, brand, month_discount_brand)
naam = f'de dicount op brand {brand} met de price {price}'
test(naam, expect, calculeted_content )
sleep(1)


brand = 'honda'
price = 500
expect= 0.0
calculeted_content = calc_discount(price, brand, month_discount_brand)
naam = f'de dicount op brand {brand} met de price {price}'
test(naam, expect, calculeted_content )

report ()