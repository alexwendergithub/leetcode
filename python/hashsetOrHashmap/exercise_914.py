from collections import Counter
from math import gcd
from functools import reduce
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        card_counts = Counter(deck)
        common_divisor = reduce(gcd, card_counts.values())
        return common_divisor >= 2