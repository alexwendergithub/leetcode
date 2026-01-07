class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        HashMap<Character, Integer> CountS = new HashMap<>();
        HashMap<Character, Integer> CountT = new HashMap<>();
	    for (char c : s.toCharArray()) {
	        CountS.put(c, CountS.getOrDefault(c, 0) + 1);
	    }
	 
	    for (char c : t.toCharArray()) {
	        CountT.put(c, CountT.getOrDefault(c, 0) + 1);
	    }
        return CountT.equals(CountS);
    }
}