class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        totalAlice = 0
        totalBob = 0
        aliceCandies = set(aliceSizes)
        bobCandies = set(bobSizes)
        for candy in aliceSizes:
            totalAlice += candy
        for candy in bobSizes:
            totalBob += candy
        for candy in aliceCandies:
            print(candy,(totalBob-totalAlice)//2+candy)
            if (totalBob-totalAlice)//2+candy in bobCandies:
                return [candy,(totalBob-totalAlice)//2+candy]
        return -1