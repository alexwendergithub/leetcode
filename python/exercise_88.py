class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pointer_nums1 = m-1
        pointer_nums2 = n-1
        pointer_current_index = m+n-1
        while pointer_nums2 >= 0:
            if pointer_nums1 >=0 and nums1[pointer_nums1] > nums2[pointer_nums2]:
                nums1[pointer_current_index] = nums1[pointer_nums1]
                pointer_nums1 = pointer_nums1-1
            else:
                nums1[pointer_current_index] = nums2[pointer_nums2]
                pointer_nums2 = pointer_nums2-1
            pointer_current_index = pointer_current_index-1