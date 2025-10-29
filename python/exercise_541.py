class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        slicing = [s[i:i+k] for i in range(0, len(s), k)]
        reverse = True
        for i in range(len(slicing)):
            if reverse:
                slicing[i] = slicing[i][::-1]
            reverse = not reverse
        return "".join(slicing)