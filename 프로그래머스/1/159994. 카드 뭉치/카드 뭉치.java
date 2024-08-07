import java.util.*;
class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "";
        
        Deque<String> q1 = new ArrayDeque<>();
        Deque<String> q2 = new ArrayDeque<>();
        List<String> tempAnswer = new ArrayList<>();
        
        
        for (String ch : cards1) {
            q1.addLast(ch);
        }
        
        for (String ch : cards2) {
            q2.addLast(ch);
        }
        
        for (int i = 0; i < goal.length; i++) {
            if (!q1.isEmpty() && q1.peekFirst().equals(goal[i])) {
                tempAnswer.add(q1.removeFirst());
            } else if(!q2.isEmpty() && q2.peekFirst().equals(goal[i])) {
                tempAnswer.add(q2.removeFirst());
            } else {
                break;
            }
        }
        
        for (int i = 0; i < tempAnswer.size(); i++ ) {
            if(tempAnswer.size() != goal.length || !tempAnswer.get(i).equals(goal[i])) {
                answer = "No";
                break;
            }
        }
        
        return answer.equals("No") ? "No" : "Yes";
    }
}