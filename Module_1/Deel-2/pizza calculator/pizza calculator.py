# Voornaam: [Jouw voornaam]
# Achternaam: [Jouw achternaam]
# Opdracht: Pizza Calculator

# aankondeging
print('-' * 37)
print('')
print("Welkom bij Ghost voor pizza!")
print('')
print("-"*36)
# variabelen
smal=8.50
medium=9.00
large=10.00
# vrgen lijs
aantaal_samlle_pizza = int(input('Hoe veel samlle pizza wilt u hebben? '))
aantaal_mediume_pizza = int(input('Hoe veel mediume pizza wilt u hebben? '))
aantaal_large_pizza = int(input('Hoe veel large pizza wilt u hebben? '))

# reken somen 
totaal_prijs_smal = aantaal_samlle_pizza * smal
totaal_prijs_medium = aantaal_mediume_pizza * medium
totaal_prijs_large = aantaal_large_pizza * large
totaal = totaal_prijs_smal + totaal_prijs_medium + totaal_prijs_large
# bon
print('')
print('')
print('-' * 37)
print (f'| Kosten voor de {aantaal_samlle_pizza} smalle pizza   {totaal_prijs_smal}')
print (f'| Kosten voor de {aantaal_mediume_pizza} mediume pizza  {totaal_prijs_medium}')
print (f'| Kosten voor de {aantaal_large_pizza} large pizza    {totaal_prijs_large}')
print('-' * 37)
print('')
print('')
print('-' * 37)
print (f"| U totalle bedrag voor \n |{aantaal_samlle_pizza} smalle pizza \n |{aantaal_mediume_pizza} mediume pizza \n |{aantaal_large_pizza} large pizza is {totaal:.2f}")
print('-' * 37)