class Solution {
    public String longestCommonPrefix(String[] strs) {
        String commonPrefix = strs[0];
        for(int i=0;i<strs.length;i++){
            int maxLengthPrefix = Math.min(commonPrefix.length(),strs[i].length());
            String newPrefix = "";
            for(int j=0;j<maxLengthPrefix;j++){
                if(commonPrefix.charAt(j)!=strs[i].charAt(j)){
                    break;
                }else{
                    newPrefix+=commonPrefix.charAt(j);
                }
            }
            commonPrefix = newPrefix;
        }
        return commonPrefix;
    }
}