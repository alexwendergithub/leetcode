class Solution {
    public int removeElement(int[] nums, int val) {
        int valCount = 0;
        int n = nums.length-1;
        for (int i=n;i>=0;i--){
            if(nums[i]==val){
                int temp = nums[i];
                nums[i] = nums[n-valCount];
                nums[n-valCount]= temp;
                valCount++;
            }
        }
        return nums.length-valCount;
    }
}