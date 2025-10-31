class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if(len(s) != len(t)):
            return False
        for letter in s:
            if letter in hashmap:
                hashmap[letter]+=1
            else:
                hashmap[letter] = 1
        for letter in t:
            if letter in hashmap:
                hashmap[letter]-=1
                if hashmap[letter]<0:
                    return False
            else:
                return False
        return True