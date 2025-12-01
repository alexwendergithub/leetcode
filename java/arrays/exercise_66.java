class Solution {
    public int[] plusOne(int[] digits) {
        int carryOn = 0;
        for(int i = digits.length-1;i>=0;i--){
            if(carryOn == 1){
                if(digits[i]==9){
                    digits[i]=0;
                    carryOn = 1;
                }else{
                    digits[i]+=1;
                    carryOn = 0;
                    break;
                }
            }else{
                if(digits[i] == 9){
                    digits[i]=0;
                    carryOn = 1;    
                }else{
                    digits[i]+=1;
                    carryOn = 0;
                    break;
                }
            }
        }


        if(carryOn == 1){
            int[] newArray = new int[digits.length + 1];
            newArray[0] = 1;
            for (int i = 1; i < digits.length; i++) {
                newArray[i] = digits[i-1];
            }
            return newArray;
        }
        return digits;
    }
}