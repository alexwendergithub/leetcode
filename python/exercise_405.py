#lembrete:se envolver bits usar bitshift
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        res = []
        hexset = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        for position in range(7, -1, -1):
            hex_digit_value = (num >> (4 * position)) & 0xF
            if res or hex_digit_value != 0:
                res.append(hexset[hex_digit_value])
        return ''.join(res)
