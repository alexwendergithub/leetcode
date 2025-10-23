hashmap = {1:1,0:0}
class Solution:

    def fib(self, n: int) -> int:
        if n in hashmap:
            return hashmap[n]
        else:
            result = self.fib(n-1) + self.fib(n-2)
            hashmap[n] = result
            return result