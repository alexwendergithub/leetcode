class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn == 0:
            return ["0:00"]
        if turnedOn == 9 or turnedOn == 10:
            return []
        res = []
        for i in range(12):
            for j in range(60):
                hour_one_count = bin(i).count('1')
                minute_one_count = bin(j).count('1')
                if hour_one_count + minute_one_count == turnedOn:
                    if j < 10:
                        j = '0'+str(j)
                    res.append(str(i)+":"+str(j))
        return res