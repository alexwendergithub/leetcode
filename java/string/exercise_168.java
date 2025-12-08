class Solution {
    public String convertToTitle(int columnNumber) {
        String column = "";
        char charachterList[] = {'Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
        while (columnNumber>26){
            int num = columnNumber%26;
            columnNumber = columnNumber/26;
            if (num == 0){
                columnNumber-=1;
            }
            column = charachterList[num]+column;
        }
        return charachterList[columnNumber]+column;   
    }
}