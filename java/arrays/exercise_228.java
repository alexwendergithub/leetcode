class Solution {
    public List<String> summaryRanges(int[] nums) {
        if(nums.length == 0){
            return new ArrayList<>();
        }
        int start = nums[0];
        int count = 0;
        List<String> res = new ArrayList<>();
        for (int i=0;i<nums.length;i++){
            if(nums[i]>start+count){
                if (start == nums[i-1]){
                    res.add(String.valueOf(start));
                }else{
                    res.add(String.valueOf(start)+"->"+String.valueOf(nums[i-1]));
                }
                start = nums[i];
                count = 0;
            }
            count++;
        }
        if(start == nums[nums.length-1]){
            res.add(String.valueOf(start));
        }else{
            res.add(String.valueOf(start)+"->"+String.valueOf(nums[nums.length-1]));
        }
        return res;
    }
}