
#vraieabelen
a=int(input("geef een hele getaal! "))
b=int(input("geef een hele getaal! "))

#statment
if a > b:
    MAX=a
    MIN=b
    print(f'(a) is groter getaal {MAX}')
elif a < b:
    MIN=a
    MAX=b
    print(f'(a) is groter getaal {MIN}')
else:
    print("(a)is gelijk aan (b)")

#print's
print(f'a is het maximum {MAX}')
print(f'b is het minmum {MIN}')