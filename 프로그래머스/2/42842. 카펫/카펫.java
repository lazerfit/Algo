import java.util.*;
class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        List<int[]> a = new ArrayList<>();
        int n = brown + yellow;
        int j = 0;
        for (int i=n;i>0;i--) {
            int[] temp = new int[2];
            if (n%i == 0) {
                j = n/i;
                temp[0] = i;
                temp[1] = j;
                
                if (i < j) {
                    break;
                } 
                a.add(temp);
                j=0;
            }
        }
        
        for (int[] e : a) {
            if ((2 * e[0]) + (2 * (e[1] - 2)) == brown) {
                answer = e.clone();
            }
        }
        
        return answer;
    }
}