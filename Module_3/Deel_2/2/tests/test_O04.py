import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from data import JOURNEY_IN_DAYS

def calcutel_travel_days(nights_one_way):
    return nights_one_way * 2

expected = JOURNEY_IN_DAYS
# expected = 11
result = int(calcutel_travel_days(4.5) + 1)
test('calcutel_travel_days - test 1',expected, result)
    


if __name__ == "__main__":
    report()