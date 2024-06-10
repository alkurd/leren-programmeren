import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from data import JOURNEY_IN_DAYS

#schrijf je test hier
def calculate_travel_days(nights_one_way):
    return nights_one_way * 2

expected = JOURNEY_IN_DAYS
result = calculate_travel_days(5)
test('calculate_travel_days - test 1',expected, result)

if __name__ == "__main__":
    report()