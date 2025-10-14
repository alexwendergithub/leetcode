class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lista = []
        for num in nums1:
            if num in nums2 and num not in lista:
                lista.append(num)
        return lista