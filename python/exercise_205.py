class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        hashmap2 = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                if t[i] != hashmap[s[i]]:
                    return False
            else:
                hashmap[s[i]] = t[i]
            if t[i] in hashmap2:
                if s[i] != hashmap2[t[i]]:
                    return False
            else:
                hashmap2[t[i]] = s[i]
        return True