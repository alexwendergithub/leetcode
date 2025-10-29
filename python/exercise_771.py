from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_counts = Counter(stones)
        count = 0
        for element in stone_counts:
            if element in jewels:
                count+=stone_counts[element]
        return count