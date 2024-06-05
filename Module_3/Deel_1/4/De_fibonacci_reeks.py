def fibonacci(a):
    a = []
    for i in range(10+1):
        if i == 0:
            a.append(0)
        elif i == 1:
            a.append(1)
        else:
            a.append(a[i-1] + a[i-2])
    return a

print(fibonacci(10))
# def stringEndWhit(strA, strB):
#     return strA.endswith(strB)
#     return strA[-len(strB):] == strB

    
# print(stringEndWhit('a c','ac'))

