import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numberPosition = new HashMap<Integer, Integer>();
        for(int i=0;i<nums.length;i++){
            if (numberPosition.containsKey(target-nums[i])){
                return new int[] {i,numberPosition.get(target-nums[i])};
            }
            numberPosition.put(nums[i],i);
        }
        return null;   
    }
}