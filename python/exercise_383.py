class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for letter in magazine:
            if letter in hashmap:
                hashmap[letter] += 1
            else:
                hashmap[letter] = 1
        for letter in ransomNote:
            if letter not in hashmap:
                return False
            else:
                hashmap[letter] -= 1
                if hashmap[letter] < 0:
                    return False
        return True