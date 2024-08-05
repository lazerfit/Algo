import java.util.ArrayDeque;
import java.util.HashMap;

class Solution {
    public int solution(String s) {
        int n = s.length();
        s+=s;
        int answer = 0;
        HashMap<Character, Character> map = new HashMap<>();
        
        map.put(')','(');
        map.put('}','{');
        map.put(']','[');
        
        A:for ( int i = 0; i < n; i++){
            ArrayDeque<Character> stack = new ArrayDeque<>();
            for ( int j=i; j<i+n;j++){
                char c = s.charAt(j);
                if(!map.containsKey(c)) {
                    stack.push(c);
                } else {
                    if(stack.isEmpty() || !stack.pop().equals(map.get(c))) {
                       continue A; 
                    }
                }
            }
            if (stack.isEmpty()){
                answer++;
            }
        }
        
        return answer;
    }
}