class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer,Integer> numbers = new HashMap<>();
        for(int i = 0;i<nums.length;i++){
            if(numbers.containsKey(nums[i])){
                if((i-numbers.get(nums[i]))<=k){
                    return true;
                }
            }
            numbers.put(nums[i],i);
        }
        return false;
    }
}