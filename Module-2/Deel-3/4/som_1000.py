# totaal = 0
# current = 50
# optel = 1
# while totaal <= 1000:
#     totaal += current                
#     print(f'{optel}. {'+'.join([str(x) for x in range(50 ,  current + 1)])} = {totaal}')
#     current += 1
#     optel += 1
###########################################################################################################
#_________________________________________________________________________________________________________#
# def points(matches):
#     total_points = 0
#     for match in matches:
#         x, y = map(int, match.split(":"))
#         if x > y:
#             total_points += 3
#         elif x == y:
#             total_points += 1
#     return total_points
# matches = ["3:1", "2:2", "0:1", "4:0", "1:2", "2:1", "3:3", "1:0", "0:4", "2:0"]
# print("Total points:", points(matches))
###########################################################################################################
#_________________________________________________________________________________________________________#
# NUMBER  = 50
# PlusNumber = 51
# optelNumber = 1
# GoalNumber = 0
# line = ''
# while GoalNumber <= 1000:
#     PlusNumber += optelNumber + NUMBER
#     print (PlusNumber)
#     GoalNumber += optelNumber
#     volgende  = input('Do you want to continue? ')
#     if volgende == 'no':
#         break
    # break
Number = 50
totaal = 50 
som =  '50'
lijn = 0 
# allles = []
while totaal < 1000:
    lijn += 1
    Number += 1
    totaal += Number
    som += f' + {Number}'
    print(f'{lijn}. {som} = {totaal}')
    # print(som)
    # volgende  = input('Do you want to continue? ')
    # if volgende == 'no':
    #     break