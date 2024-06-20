import time
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_FOOD_HORSE_COPPER_PER_DAY, COST_TENT_GOLD_PER_WEEK, COST_HORSE_SILVER_PER_DAY,COST_INN_HUMAN_SILVER_PER_NIGHT, COST_INN_HORSE_COPPER_PER_NIGHT

from math import ceil

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return amount * 0.1
    

def silver2gold(amount:int) -> float:
    return amount * 0.2

def copper2gold(amount:int) -> float:
    copper = amount * 0.02
    return copper

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    amount = 0
    amount += copper2gold(personCash.get('copper', 0))
    amount += silver2gold(personCash.get('silver', 0))
    amount += platinum2gold(personCash.get('platinum', 0))
    amount += personCash.get('gold', 0)
    return amount
    # return copper2gold(copper) + silver2gold(silver) + platinum2gold(platinum)

    

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    # total_days = JOURNEY_IN_DAYS
    total_food_cost_humans = people * COST_FOOD_HUMAN_COPPER_PER_DAY * JOURNEY_IN_DAYS
    total_food_cost_horses = horses * COST_FOOD_HORSE_COPPER_PER_DAY * JOURNEY_IN_DAYS
    total_food_cost = total_food_cost_humans + total_food_cost_horses
    total_food_cost_copper = round(copper2gold(total_food_cost),2)
    return total_food_cost_copper
    

##################### O06 #####################
def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    nieuw_list = []
    for item in  list:
        if key in item and item[key] == value:
            nieuw_list.append(item)
    return nieuw_list

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)
    

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends,'shareWith', True)
    

def getAdventuringFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'adventuring', True) and getFromListByKeyIs(friends,'shareWith', True)
    

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return ceil(people / 2)
    # if people % 2 != 0:
    #     neededHorses += 1
    # return int(neededHorses)
   

def getNumberOfTentsNeeded(people:int) -> int:
    neededTesnts = people / 3
    return ceil(neededTesnts)
    # if people % 3 != 0:
    #     neededTesnts += 1
    # return int(neededTesnts)
    

def getTotalRentalCost(horses:int, tents:int) -> float:

    # week_dagen = 7
    total_weken = ceil(JOURNEY_IN_DAYS / 7 )# 7 dagen van de wwek 

    cost_horses = silver2gold(COST_HORSE_SILVER_PER_DAY) * horses * JOURNEY_IN_DAYS
    cost_tents = COST_TENT_GOLD_PER_WEEK * tents * total_weken
    total_rental_cost = cost_horses + cost_tents
    return round(total_rental_cost,2)

   

##################### O08 #####################

def getItemsAsText(items: list) -> str:
    # string_list = []
    # for item in items:
    #     string_list.append(f"{item['amount']}{item['unit']} {item['name']}")
    # if len(string_list) == 1:
    #     return string_list[0]
    # else:
    #     return ', '.join(string_list[:-1]) +' & '+ string_list[-1]
    
    string = ''
    for index, item in enumerate(items):
        string += f"{item['amount']}{item['unit']} {item['name']}"
        if index < len(items) -2:
            string += ', '
        elif index < len(items) -1:
            string += ' & '
    return string

            

def getItemsValueInGold(items:list) -> float:
    total_gold = 0.0
    for item in items:
        amount_1 = item['amount']
        amount_2 = item['price']['amount']
        total = amount_1 * amount_2

        # # amount = item['amount']
        # price = item['price']
        # totel = amount * price['amount']
        # totel = item['amount'] * item['price']['amount']
        
        if item['price']['type'] == 'copper':
            total_gold += copper2gold(total)
        elif item['price']['type'] == 'silver':
            total_gold += silver2gold(total)
        elif item['price']['type'] == 'platinum':
            total_gold += platinum2gold(total)
        elif item['price']['type'] == 'gold':
            total_gold += total
    
    return round(total_gold, 2)
    

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    total_cash = 0.0
    for person in people:
        if 'cash' in person:
            total_cash += getPersonCashInGold(person['cash'])
    return round(total_cash,2)

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    list = []
    for investor in investors:
        if investor['profitReturn'] <= 10:
            list.append(investor)
    return list

def getAdventuringInvestors(investors:list) -> list:
    list = []
    for investor in getInterestingInvestors(investors):
        if investor['adventuring'] == True:
            list.append(investor)
    return list

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    adventuring_investors = getAdventuringInvestors(investors)
    num_investors = len(adventuring_investors)
    total_gear_cost = getItemsValueInGold(gear) * num_investors
    total_food_cost = getJourneyFoodCostsInGold(num_investors, num_investors)
    total_rental_cost = getTotalRentalCost(num_investors, num_investors)
    total_costs = total_gear_cost + total_food_cost + total_rental_cost
    return round(total_costs,2)

    

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    total_cost_per_night = (people * silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT)) + (horses * copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT))
    max_nights = leftoverGold // total_cost_per_night
    return int(max_nights)
    

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    total_cost_per_night = (people * silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT)) + (horses * copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT))
    total_cost = total_cost_per_night * nightsInInn
    return round(total_cost,2)

    # total_cost = total_cost_per_night * getMaxAmountOfNightsInInn(nightsInInn)
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()