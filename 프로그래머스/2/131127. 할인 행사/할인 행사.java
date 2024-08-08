import java.util.*;
class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        HashMap<String, Integer> map = new HashMap<>();
        
        for (int i = 0; i < want.length; i++) {
            map.put(want[i], number[i]);
        }
        
        A:for (int i =0;i< discount.length-9;i++ ) {
            HashMap<String, Integer> dis = new HashMap<>();
            for (int j=i;j<i+10;j++) {
                dis.put(discount[j],dis.getOrDefault(discount[j],0) + 1);
            }
            for (String str:want) {
                if(map.get(str) != dis.getOrDefault(str,0)) {
                    continue A;
                }
            }
            answer++;
        }
        
        return answer;
    }
}