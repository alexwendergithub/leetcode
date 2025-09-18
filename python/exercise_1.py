class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        pointer = 0
        while pointer<(len(nums)):
            if target-nums[pointer] in hashmap:
                return [hashmap[target-nums[pointer]],pointer]
            if nums[pointer] not in hashmap:
                hashmap[nums[pointer]] = pointer
            pointer = pointer+1
        
        return 0