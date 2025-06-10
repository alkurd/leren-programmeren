import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HUMAN_COPPER_PER_DAY,COST_FOOD_HORSE_COPPER_PER_DAY, COST_HORSE_SILVER_PER_DAY, COST_TENT_GOLD_PER_WEEK

##################### O03 #####################

def copper2silver(amount:int) -> float:
    silver =  amount / 10

    return silver 
    

def silver2gold(amount:int) -> float:
    gold = amount / 5
    return gold
    

def copper2gold(amount:int) -> float:
    gold = amount / 50
    return gold

def platinum2gold(amount:int) -> float:
    gold = amount * 25
    return gold

def getPersonCashInGold(personCash:dict) -> float:
    tottal_gold = 0 
    if 'copper' in personCash:
        tottal_gold += copper2gold(personCash['copper'])
    if 'silver' in personCash:
        tottal_gold += silver2gold(personCash['silver'])
    if 'platinum' in personCash:
        tottal_gold += platinum2gold(personCash['platinum'])
    if 'gold' in personCash:
        tottal_gold += personCash['gold']

    return tottal_gold
    pass

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:

    tottal_food_cost = (people * COST_FOOD_HUMAN_COPPER_PER_DAY + horses * COST_FOOD_HORSE_COPPER_PER_DAY) * JOURNEY_IN_DAYS
    tottal_food_cost_in_gold = round(copper2gold(tottal_food_cost),2)
    return tottal_food_cost_in_gold

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    nieuwe_list = []
    for item in list:
        if key in item and item[key] == value:
            nieuwe_list.append(item)
    return nieuwe_list


def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)
    

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    nieuwe_list = []
    for friend in friends:
        if friend['adventuring'] == True and friend['shareWith'] == True:
            nieuwe_list.append(friend)
    return nieuwe_list
    

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)
    pass

def getNumberOfTentsNeeded(people:int) -> int:
        return math.ceil(people / 3)
    

def getTotalRentalCost(horses:int, tents:int) -> float:
    totall_weeks = math.ceil(JOURNEY_IN_DAYS / 7)
    tent_cost = totall_weeks * ( COST_TENT_GOLD_PER_WEEK * tents)
    horses_cost = silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS * horses
    totall_cost = tent_cost + horses_cost 
    return round(totall_cost,2)
    pass

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    string = ''
    for index , item in enumerate(items):
    # for item in items:
        string += f"{item['amount']}{item['unit']}{item['name']}"
        if index < len(items) -2:
            string += ', '
        elif index <len(items) -1:
            string += '& '
        return string 
        pass

def getItemsValueInGold(items:list) -> float:
    total_gold = 0.0
    for item in items:
        amount_1 = item['amount']
        amount_2 = item['price']['amount']
        total = amount_1 * amount_2

        if item['price'] ['type'] == 'copper':
            total_gold +=copper2gold (total)
        elif item['price'] ['type'] == 'silver':
            total_gold +=silver2gold (total)
        elif item['price'] ['type'] == 'platinum':
            total_gold +=platinum2gold (total)
        elif item['price'] ['type'] == 'gold':
            total_gold += total
    return round(total_gold, 2)
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