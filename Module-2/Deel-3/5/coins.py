# name of student: 
# number of student:
# purpose of program: 
# structure of program: 

coinValues = [500,200,100,50,20,10,5,2,1] #

toPay = int(float(input('Amount to pay: ')) * 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #

coinsReturned = {}

while change > 0 and len(coinValues) > 0: #

  coinValue = coinValues.pop(0) #
  nrCoins = change // coinValue #nrCoins is changed 

  if nrCoins > 0: #
    print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
    nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
    change -= nrCoinsReturned * coinValue #
    coinsReturned[coinValue] = nrCoinsReturned

if change > 0: #
  print('Change not returned: ', str(change) + ' cents left to pay')
  for coinValue, nrCoinsReturned in coinsReturned.items():
        print(f'You have returned {nrCoinsReturned} coins of {coinValue} cents')

 #
else:
  print('done')
  for coinValue, nrCoinsReturned in coinsReturned.items():
        print(f'You have returned {nrCoinsReturned} coins of {coinValue} cents')
   #