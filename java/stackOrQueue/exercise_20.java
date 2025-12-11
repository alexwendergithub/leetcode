import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> fila = new Stack<>();
        char[] chars = s.toCharArray();
        for(int i=0;i<chars.length;i++){
            if((chars[i] == '(') || (chars[i] == '{') || (chars[i] == '[')){
                fila.push(chars[i]);
            }else{
                if(fila.isEmpty()){
                    return false;
                }
                if(chars[i]==')'){
                    if(fila.pop()!='('){
                        return false;
                    }
                }else{
                    if(chars[i]=='}'){
                        if(fila.pop()!='{'){
                            return false;
                        }
                    }else{
                        if(chars[i]==']'){
                            if(fila.pop()!='['){
                                return false;
                            }
                        }
                    }
                }
            }
        }
        return fila.isEmpty();
    }
}