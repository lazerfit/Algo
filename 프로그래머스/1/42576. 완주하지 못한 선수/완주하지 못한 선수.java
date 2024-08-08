import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> p = new HashMap<>();
        
        for (String str : participant) {
            if(p.get(str) != null) {
                p.put(str,p.get(str)+1);
            } else {
                p.put(str,1);
            }
        }
        
        for (String str : completion) {
            if(p.get(str) != 1) {
                p.put(str,p.get(str)-1);
            } else {
                p.remove(str);
            }
        }
        
        return p.keySet().stream().findFirst().orElse(null);
    }
}