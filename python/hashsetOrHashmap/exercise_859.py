class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        letters = []
        dup = False
        dif = 0
        difs = []
        difg = []
        for i in range(len(s)):
            if s[i] in letters:
                dup = True
            else:
                letters.append(s[i])
            if s[i] != goal[i]:
                dif+=1
                difs.append(s[i])
                difg.append(goal[i])
                if dif>=3:
                    return False
        difs.sort()
        difg.sort()
        return (dif==0 and dup) or (dif==2 and (difs == difg))