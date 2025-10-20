class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        i, j = len(num1) - 1, len(num2) - 1
        result = []
        carry = 0
        while i >= 0 or j >= 0 or carry:
            digit1 = 0 if i < 0 else int(num1[i])
            digit2 = 0 if j < 0 else int(num2[j])
            carry, digit_sum = divmod(digit1 + digit2 + carry, 10)
            result.append(str(digit_sum))
            i -= 1
            j -= 1
        return "".join(result[::-1])