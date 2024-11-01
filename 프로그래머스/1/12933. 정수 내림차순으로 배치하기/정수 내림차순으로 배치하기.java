import java.util.*;
class Solution {
    public long solution(long n) {
        String answer = "";
        String[] s = String.valueOf(n).split("");

        Arrays.sort(s, Collections.reverseOrder());

        for (int i=0;i<s.length;i++) {
            answer += s[i];
        }
        
        return Long.valueOf(answer);
    }
}