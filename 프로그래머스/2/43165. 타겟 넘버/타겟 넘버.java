import java.util.*;
class Solution {
    static int n;
    static int answer;
    
    static void backTracking(int idx, int sum, int[] numbers, int target) {
        if (idx == n) {
            if (sum == target) answer++;
            return;
        }
        
        backTracking(idx + 1, sum + numbers[idx], numbers ,target);
        backTracking(idx + 1, sum - numbers[idx], numbers ,target);
    }
    
    public int solution(int[] numbers, int target) {
        n = numbers.length;
        answer = 0;
        backTracking(0,0,numbers,target);
        
        return answer;
    }
}