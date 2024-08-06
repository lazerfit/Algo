import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Deque<Integer> stack = new ArrayDeque<>();
        
        for (int i : arr) {
            if (stack.isEmpty() || !stack.peekLast().equals(i)) {
                stack.addLast(i);            
            } 
        }
        
        int[] answer = new int[stack.size()];
        int stackSize = stack.size();
        
        for ( int i = 0; i < stackSize; i++) {
            answer[i] = stack.removeFirst();
        }
        
        return answer;
    }
}