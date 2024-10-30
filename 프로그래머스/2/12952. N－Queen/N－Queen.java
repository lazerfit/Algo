import java.util.*;
class Solution {
    static boolean[] width;
    static boolean[] diagonal1;
    static boolean[] diagonal2;
    static int N;
    
    static int getAns(int y) {
        int ans = 0;
        if (y == N) {
            ans++;
        }
        
        for (int i=0;i<N;i++) {
            if (width[i] || diagonal1[i + y] || diagonal2[i - y + N])
                continue;
            
            width[i] = diagonal1[i + y] = diagonal2[i - y + N] = true;
            ans += getAns(y + 1);
            width[i] = diagonal1[i + y] = diagonal2[i - y + N] = false;
        }
        
        return ans;
    }
    
    public int solution(int n) {
        N = n;
        width = new boolean[n];
        diagonal1 = new boolean[n * 2];
        diagonal2 = new boolean[n * 2];
        
        return getAns(0);
    }
}