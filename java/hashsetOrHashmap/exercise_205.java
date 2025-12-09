class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character,Character> StoT = new HashMap<>();
        HashMap<Character,Character> TtoS = new HashMap<>();
        for(int i=0;i<s.length();i++){
            char sCurrent = s.charAt(i);
            char tCurrent = t.charAt(i);
            if(StoT.containsKey(sCurrent)){
                if(TtoS.containsKey(tCurrent)){
                    if(TtoS.get(tCurrent)!=sCurrent || StoT.get(sCurrent)!=tCurrent){
                        return false;
                    }
                }else{
                    return false;
                }
            }else{
                if(TtoS.containsKey(tCurrent)){
                    return false;
                }else{
                    StoT.put(sCurrent,tCurrent);
                    TtoS.put(tCurrent,sCurrent);
                }
            }
        }
        return true;
    }
}