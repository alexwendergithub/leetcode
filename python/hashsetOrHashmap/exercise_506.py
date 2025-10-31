4.py
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        gold = None
        silver = None
        bronze = None
        hashmap = []
        for value in score:
            hashmap.append(value)
        hashmap.sort()
        hashmap.reverse()
        for i in range(len(hashmap)):
            for j in range(len(score)):
                if hashmap[i] == score[j]:
                    if i < 3:
                        values = ["Gold Medal","Silver Medal","Bronze Medal"]
                        score[j] = values[i]
                        break
                    score[j] = str(i+1)
                    break
        return score