class Solution {
    public int removeDuplicates(int[] nums) {
        int uniqueIndex = 0;
        for (int element : nums) {
            if (uniqueIndex == 0 || element != nums[uniqueIndex - 1]) {
                nums[uniqueIndex] = element;
                uniqueIndex++;
            }
        }
        return uniqueIndex;
    }
}