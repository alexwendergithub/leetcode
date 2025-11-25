//tambem é possivel fazer com calculos tbm, o que seria um pouco mais otimizado
class Solution {
    public boolean isPalindrome(int x) {
        String numString = String.valueOf(x);
        int left = 0;
        int right = numString.length()-1;
        if(numString.length() == 1) 
			return true;
        if(x < 0){
            return false;
        }
        for (;left<right;){
            if(numString.charAt(left)!=numString.charAt(right)){
                return false;
            }
            left+=1;
            right-=1;
        }
        return true;
    }
}