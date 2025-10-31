class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candyTypes = 0
        lista = []
        for candy in candyType:
            if candy not in lista:
                candyTypes += 1
                lista.append(candy)
            if candyTypes > int(len(candyType)/2):
                return int(len(candyType)/2)
        return candyTypes
#class Solution:
#    def distributeCandies(self, candyType: List[int]) -> int:
#        return min(len(set(candyType)), len(candyType) // 2)