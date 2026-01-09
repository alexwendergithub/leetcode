class NumArray {
    List<Integer> sums = new ArrayList<>();
    public NumArray(int[] nums) {
        int sum = 0;
        for(int num: nums){
            sum +=num;
            sums.add(sum);
        }
    }
    
    public int sumRange(int left, int right) {
        if(left==0){
            return sums.get(right);
        }
        return(sums.get(right)-sums.get(left-1));
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */