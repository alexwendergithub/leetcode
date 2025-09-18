class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        stack = []
        for letter in s:
            if letter == "(" or letter == "{" or letter == "[":
                stack.append(letter)
            else:
                if not len(stack):
                    return False
                if (stack[-1] == "(" and letter == ")") or (stack[-1] == "{" and letter == "}") or (stack[-1] == "[" and letter == "]"):
                    stack.pop()
                else:
                    print([stack,letter])
                    return False
        if len(stack):
            return False
        return True
