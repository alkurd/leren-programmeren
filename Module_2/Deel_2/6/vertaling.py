# woordenboek = {
#     'one': 'een', 'two': 'twee', 'three': 'drie', 'four': 'vier'
# }

# # verhaal = input('voer het verhaal? ')
# verhaal = ' one vinger can not cross tow finger can cross three fingers can cross four fingers can not cross'
# # for word in woordenboek:
# verhaal = verhaal.split(' ')
# # for tekst in woordenboek:
# #     verhaal = verhaal.replace(tekst, woordenboek[tekst])
# #     splitsplit
# # vertaling  = verhaal.replace(woordenboek,'')
# print (verhaal) 

woordenboek = {
    'one': 'een', 'two': 'twee', 'three': 'drie', 'four': 'vier'
}

verhaal = 'one finger can not cross, two finger can cross, three fingers can cross, twosides four fingers can not cross'
nieuwe_verhaal = ''
verhaal_woorden = verhaal.split()
# print (verhaal_woorden)
for woord in verhaal_woorden:
    # print (woord)
    if woord in woordenboek:
        verhaal_worden = woordenboek[woord]
        nieuwe_verhaal += verhaal_worden + ' '
        
    else:
        nieuwe_verhaal += woord +' '
        
print(nieuwe_verhaal)




    # 

