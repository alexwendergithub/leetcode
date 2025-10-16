class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = Counter(s)
        res = -1
        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i
        return res