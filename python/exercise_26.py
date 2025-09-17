#could have used hashmap(redo)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        final_element = len(nums)-1
        pointer = 0
        if final_element == 0:
            return 1
        while pointer <= final_element-1:
            if nums[pointer] == nums[pointer+1]:
                nums.pop(pointer+1)
                final_element = final_element-1
            else:
                pointer = pointer+1