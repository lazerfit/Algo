class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        
        
        for (double i : numbers ) {
            answer += i;
        }
        
        return answer/numbers.length;
    }
}