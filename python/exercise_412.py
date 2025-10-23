class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            res_aux = ""
            if i % 3 == 0:
                res_aux+="Fizz"
            if i % 5 == 0:
                res_aux+="Buzz"
            if res_aux == "":
                res_aux+=str(i)
            res.append(res_aux)
        return res