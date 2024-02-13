for uur in range(1, 25):
    periode = 'AM'
    if uur > 12:
        periode = 'PM'
        uur -= 12
    print(f'Uur: {uur} {periode}')
