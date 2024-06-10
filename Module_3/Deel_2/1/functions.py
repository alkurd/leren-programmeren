import time
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_FOOD_HORSE_COPPER_PER_DAY, COST_TENT_GOLD_PER_WEEK, COST_HORSE_SILVER_PER_DAY
from math import ceil

##################### O03 #####################

def copper2silver(amount:int) -> float:
    siver = amount / 10
    return siver
    

def silver2gold(amount:int) -> float:
    gold = amount / 5
    return gold

def copper2gold(amount:int) -> float:
    silver = copper2silver(amount)
    gold = silver2gold(silver)
    return gold

def platinum2gold(amount:int) -> float:
    platinum =   25*amount
    return int(platinum) 

def getPersonCashInGold(personCash:dict) -> float:
    copper = personCash.get('copper',0)
    silver = personCash.get('silver',0)
    gold = personCash.get('gold',0)
    platinum = personCash.get('platinum',0)

    gold_from_copper = copper2gold(copper)
    gold_from_silver = silver2gold(silver)
    gold_from_platinum = platinum2gold(platinum)
    totaalGold = gold + gold_from_copper + gold_from_silver + gold_from_platinum
    return totaalGold
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
    pass

def getNumberOfTentsNeeded(people:int) -> int:
    neededTesnts = people / 3
    if people % 3 != 0:
        neededTesnts += 1
    return int(neededTesnts)
    pass

def getTotalRentalCost(horses:int, tents:int) -> float:

    week_dagen = 7
    total_weken = ceil(JOURNEY_IN_DAYS / week_dagen) 

    cost_horses = silver2gold(COST_HORSE_SILVER_PER_DAY) * horses * JOURNEY_IN_DAYS
    cost_tents = COST_TENT_GOLD_PER_WEEK * tents * total_weken
    total_rental_cost = cost_horses + cost_tents
    return round(total_rental_cost,2)

    pass

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    pass

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