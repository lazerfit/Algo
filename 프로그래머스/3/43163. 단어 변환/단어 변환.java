import java.util.*;
class Solution {
    static int answer;
    static boolean[] visited;
    static String[] Words;
    
    static void back(int cnt, String now, String target) {
        if (cnt > Words.length) return;
        
        else if (now.equals(target)) {
            answer = cnt;
            return;
        }
        
        for (int i=0;i<Words.length;i++) {
            if (!visited[i]) {
                if (isValid(now, Words[i])) {
                    visited[i] = true;
                    back(cnt + 1, Words[i], target);
                    visited[i] = false;
                }    
            }
        }
    }
    
    static boolean isValid(String now, String target) {
        int cnt = 0;
        for (int i=0;i<now.length();i++) {
            if (cnt > 1) {
                break;
            } 
            else if (now.charAt(i) != (target.charAt(i))) cnt++;
        }
        
        return cnt == 1 ? true : false;
    }
    
    public int solution(String begin, String target, String[] words) {
        answer = 0;
        visited = new boolean[words.length];
        Words = words;
        
        back(0,begin, target);
        
        return answer;
    }
}