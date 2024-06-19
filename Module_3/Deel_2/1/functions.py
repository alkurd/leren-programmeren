import time
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_FOOD_HORSE_COPPER_PER_DAY, COST_TENT_GOLD_PER_WEEK, COST_HORSE_SILVER_PER_DAY
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
    total_days = JOURNEY_IN_DAYS
    total_food_cost_humans = people * COST_FOOD_HUMAN_COPPER_PER_DAY * total_days
    total_food_cost_horses = horses * COST_FOOD_HORSE_COPPER_PER_DAY * total_days
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
    neededHorses = people / 2
    if people % 2 != 0:
        neededHorses += 1
    return int(neededHorses)
   

def getNumberOfTentsNeeded(people:int) -> int:
    neededTesnts = people / 3
    if people % 3 != 0:
        neededTesnts += 1
    return int(neededTesnts)
    

def getTotalRentalCost(horses:int, tents:int) -> float:

    week_dagen = 7
    total_weken = ceil(JOURNEY_IN_DAYS / week_dagen) 

    cost_horses = silver2gold(COST_HORSE_SILVER_PER_DAY) * horses * JOURNEY_IN_DAYS
    cost_tents = COST_TENT_GOLD_PER_WEEK * tents * total_weken
    total_rental_cost = cost_horses + cost_tents
    return round(total_rental_cost,2)

   

##################### O08 #####################

def getItemsAsText(items: list) -> str:
    string = []
    for item in items:
        string.append(f"{item['amount']}{item['unit']} {item['name']}")
    if len(string) == 1:
        return string[0]
    else:
        return ', '.join(string[:-1]) +' & '+ string[-1]
        
        
    
    

def getItemsValueInGold(items:list) -> float:
    total_gold = 0
    for item in items:
        amount_1 = item['amount']
        amount_2 = item['price']['amount']
        total = float(amount_1) * amount_2
        
        if item['price']['type'] == 'copper':
            total_gold += copper2gold(total)
        elif item['price']['type'] == 'silver':
            total_gold += silver2gold(total)
        elif item['price']['type'] == 'platinum':
            total_gold += platinum2gold(total)
        elif item['price']['type'] == 'gold':
            total_gold += total
    
    return total_gold
    

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
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