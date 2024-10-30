import java.util.*;
class Solution {
    private static int[] width;
    private static int answer;
    private static int N;
    private static void back(int y) {
        if (y == N)
            answer++;
        
        else {
            for (int i=0;i<N;i++) {
                width[y] = i;
                if(valid(y)) {
                    back(y + 1);
                }
            }
        }
    }
    
    private static boolean valid(int y) {
        for (int i =0;i<y;i++) {
            if (width[y] == width[i]) return false;
            if (Math.abs(y - i) == Math.abs(width[y] - width[i])) return false;
        }
        
        return true;
    }
    
    public int solution(int n) {
        answer = 0;
        N = n;
        width = new int[n];
        back(0);
        return answer;
    }
}