import java.util.*;
class Solution {
    public int solution(String s) {
        int answer = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        
        String[] str = s.split(" ");
        
        for (String ch : str) {
            if(!ch.equals("Z")) {
                int i = Integer.parseInt(ch);
                stack.addLast(i);
                answer += i;
            } else {
                int z = stack.removeLast();
                answer -= z;
            }
        }
        
        return answer;
    }
}