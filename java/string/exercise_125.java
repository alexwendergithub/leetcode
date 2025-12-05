class Solution {
    public boolean isPalindrome(String s) {
        String lettersOnly = s.toLowerCase().replaceAll("[^0-9a-zA-Z]", ""); 
        String reversedStr = new StringBuilder(lettersOnly).reverse().toString();
        return lettersOnly.equalsIgnoreCase(reversedStr);
    }
}