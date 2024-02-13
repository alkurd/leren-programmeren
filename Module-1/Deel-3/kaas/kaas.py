gelle_kaas=input('is de kaas geel? ')
if gelle_kaas == 'ja':
    gaten_in_de_kaas=input('zitten er gatten in? ')
    if gaten_in_de_kaas=='ja':
        belachlijk_duur=input('is de kaas belachlijk duur? ')
        if belachlijk_duur == 'ja':
            print('emmenthaler')
        elif belachlijk_duur == 'nee':
            print('leerdammer')
    elif gaten_in_de_kaas =='nee':
        harde_kaas=input('is de kaas hard als steen? ')
        if harde_kaas=='ja':
            print('parmigiano reggiano')
        elif harde_kaas == 'nee':
            print('gouds kaas')    
elif gelle_kaas=='nee':
    schimmel_kaas=input('heeft de kaas blauwe schimmels? ')
    if schimmel_kaas =='ja':
        warme_kaas=input('heeft de kaas korts? ')
        if warme_kaas=='ja':
            print('blue de rochbaron')
        elif warme_kaas=='nee':
            print("foume d'ambert")
    elif schimmel_kaas == 'nee':
        warme_kaas=input('heeft de kaas korts? ')
        if warme_kaas=='ja':
            print('camembert')
        elif warme_kaas== 'nee':
            print('mozzarella')