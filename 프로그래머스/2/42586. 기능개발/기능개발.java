import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int n = speeds.length;
        Deque<Double> stack = new ArrayDeque<>();
        List<Integer> answer = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            int x = progresses[i];
            int y = speeds[i];
            double z = Math.ceil((100.0 - x)/y);
            stack.addLast(z);  
        }
        
        while(stack.size() > 0) {
            int count = 1;
            double x = stack.removeFirst();
            while (stack.size() > 0 && x >= stack.peekFirst()) {
                count++;
                stack.removeFirst();
            }
            answer.add(count);
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}