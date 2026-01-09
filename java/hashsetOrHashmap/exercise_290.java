class Solution {
    public boolean wordPattern(String pattern, String s) {
        char[] patternLetters = pattern.toCharArray();
        String[] sWords = s.split(" ");
        if (sWords.length!=patternLetters.length){
            return false;
        }

        HashMap<String,Character> a = new HashMap<>();
        HashMap<Character,String> b = new HashMap<>();
        for(int i=0;i<sWords.length;i++){
            if(a.containsKey(sWords[i])){
                if(a.get(sWords[i])!=patternLetters[i]){
                    return false;
                }
            }
            a.put(sWords[i],patternLetters[i]);

            if(b.containsKey(patternLetters[i])){
                if(!b.get(patternLetters[i]).equals(sWords[i])){
                    return false;
                }
            }
            b.put(patternLetters[i],sWords[i]);
        }
        return true;
    }
}