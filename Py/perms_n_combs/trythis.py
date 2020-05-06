from itertools import combinations, permutations
from pprint import pprint

LETTERS = 'ab'
DIGITS = '0123'

def aabc1(letters=LETTERS, digits=DIGITS):
    """Generate the distinct 5-character strings consisting of four
    letters (exactly one of which is repeated) and one digit.

    """
    for a, b in permutations(digits, 2):   # Three letters (a repeated).
        for c in letters:                   # One digit.
           result = [a, b]
           result.append(c)
           yield ''.join(result)

pprint(list(aabc1()))
