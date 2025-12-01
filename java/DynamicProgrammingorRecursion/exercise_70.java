//da pra adicionar um array salvando os resultados
class Solution {
    public int climbStairs(int n) {
        if (n == 0 || n == 1){
            return 1;
        }
        return this.climbStairs(n-1)+this.climbStairs(n-2);
    }
}