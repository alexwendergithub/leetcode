class Solution {
    public boolean isHappy(int n) {
        Set<Integer> seen = new HashSet<>();
        while(!seen.contains(n)){
            seen.add(n);
            int aux = 0;
            while(n!=0){
                aux+=(int)(n%10)*(int)(n%10);
                n/=10;
            }
            n = aux;
            if(n==1){
                return true;
            }
        }
        return false;
    }
}