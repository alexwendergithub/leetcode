#poderia so usar um hashmap contando os valores tbm pra garantir que a quantidade de valores esteja certa
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lista = []
        for num in nums1:
            if num in nums2:
                lista.append(num)
                nums2.remove(num)
        return lista