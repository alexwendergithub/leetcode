#usar numero ao inves de transformar pra string teria um desempenho melhors
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left,right+1):
            lista = list(str(num))
            print(lista)
            if "0" in lista:
                continue
            selfDividing = True
            for div in lista:
                if num%int(div):
                    selfDividing = False
            if selfDividing:
                res.append(num)
        return res