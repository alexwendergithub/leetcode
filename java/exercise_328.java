class Solution {
    public int[] countBits(int n) {
        int bitCountList[] = new int[n+1];
        for(int i=0;i<=n;i++){
            bitCountList[i] = Integer.bitCount(i);
        }
        return bitCountList;
    }
}