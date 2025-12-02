class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int pointer1 = m-1;
        int pointer2 = n-1;
        for(int i = nums1.length-1;i>=0;i--){
            if(pointer1<0){
                nums1[i] = nums2[pointer2];
                pointer2--;
            }else{
                if(pointer2<0){
                    nums1[i] = nums1[pointer1];
                    pointer1--;                
                }else{
                    if(nums1[pointer1]>nums2[pointer2]){
                        nums1[i] = nums1[pointer1];
                        pointer1--;
                    }else{
                        nums1[i] = nums2[pointer2];
                        pointer2--;
                    }
                }
            }

        }

        return;
    }
}