class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False
        hashmap = {}
        hashmap2 = {}
        for i in range(len(pattern)):
            if pattern[i] not in hashmap:
                hashmap[pattern[i]] = s[i]               
            if s[i] not in hashmap2:
                hashmap2[s[i]] = pattern[i]
        for i in range(len(pattern)):
            if not(hashmap[pattern[i]] == s[i] and hashmap2[s[i]] == pattern[i]):
                return False
        return True