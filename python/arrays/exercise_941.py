class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        increassing = True
        decreassing = False
        prev = -1
        if arr[1]<arr[0]:
            return False
        for i in range(len(arr)):
            if arr[i]==prev:
                return False
            elif arr[i]<prev and increassing:
                decreassing = True
                increassing = False
            elif arr[i]>prev and not increassing:
                return False
            prev = arr[i]
        return decreassing