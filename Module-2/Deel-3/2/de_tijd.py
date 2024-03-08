uur = 1
while uur <= 24:
    if uur <= 11:
        print(f"{uur} AM")
    elif uur == 12:
        print(f"{uur} PM")
    elif uur <= 24:
        print(f"{uur-12} PM")
    else:
        print(f"{uur-12} AM")
    uur += 1