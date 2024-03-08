# import random

# # def genereer(kleuren, hoge_karten, nummer):

# kleuren = ('harten', 'klaveren', 'schoppen' , 'ruiten')
# hoge_karten = ('Aas', 'Joker', 'Vrouw', 'Heer')
# nummer = random.randint (2,11)
# willekeurige_kleur = random.choice(kleuren)

# for _ in range(7):
#     print(f"{nummer}  {willekeurige_kleur}")
#     nummer += 1
    



import random

# def generate_cards():
kleuren = ['Harten', 'Klaveren', 'Schoppen' , 'Ruiten']
ranks = ["Aas", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Boer", "Vrouw", "Heer"]
# spaicals = 'Zwarte Joker', 'Rode Joker'
cards = ['Zwarte Joker', 'Rode Joker']
for kleur in kleuren:
    for rank in ranks:
        cards.append(f"{rank} of {kleur}")    
random.shuffle(cards)
# aantal_cards = len(cards)
print('deck ',len(cards),cards)
print()
nr = 7
for aantal_spel_cardes in range(nr): 
    speel_cards = cards.pop(0)
    print('kaart',aantal_spel_cardes + 1,':', speel_cards)

    # return cards
# cards = generate_cards()
print()
# aantal_cards = len(cards)
print('deck ',len(cards),cards)
























# import random

# def genereer():
#     kleuren = ('harten', 'klaveren', 'schoppen', 'ruiten')
#     hoge_kaarten = ('Aas', 'Joker', 'Vrouw', 'Heer')

#     willekeurige_kleur = random.choice(kleuren)
#     willekeurig_nummer = random.randint(2, 10)

#     print(f"{willekeurig_nummer}  {willekeurige_kleur}")

# # Vijf willekeurige kaarten afdrukken
# for _ in range(5):
#     genereer()
