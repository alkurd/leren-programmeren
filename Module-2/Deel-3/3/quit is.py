teller = 0
while True:
    vraag = input('What do you want to do? ')
    teller += 1
    if vraag == 'quit':
        break
print('De vraag is', teller, 'keer gesteld.')