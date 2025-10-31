class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap = {}
        count = 0
        minCount = -1
        wordMinCount = []
        for word in list1:
            hashmap[word] = count
            count+=1
        count = 0
        for word in list2:
            if word in hashmap:
                if minCount == -1:
                    minCount = hashmap[word]+count
                    wordMinCount.append(word)
                elif hashmap[word]+count < minCount:
                    minCount = hashmap[word]+count
                    wordMinCount = []
                    wordMinCount.append(word)
                elif hashmap[word]+count == minCount:
                    wordMinCount.append(word)
            count+=1
        return wordMinCount