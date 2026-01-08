/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        if(n == 1){
            return 1;
        }
        int left = 1;
        int right = n;
        int firstBad = -1;
        int middle;
        while(left <= right){
            middle = left+(right-left)/2;
            if(isBadVersion(middle)){
                firstBad = middle;
                right = middle-1;
            }
            else{
                left = middle+1;
            }
        }
        return firstBad;
    }
}