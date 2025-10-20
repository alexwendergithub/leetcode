#possivel melhorar fazendo pre busca no array pelos valores e salvando a posicao
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num1 in nums1:
            res_num = -1
            num_found = False
            for num2 in nums2:
                if num1 == num2:
                    num_found = True
                if num_found == True and num2>num1:
                    res_num = num2          
                    break
            res.append(res_num)
        return res