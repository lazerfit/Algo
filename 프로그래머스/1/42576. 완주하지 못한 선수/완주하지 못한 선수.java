import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> p = new HashMap<>();
        
        for (String str : completion) {
            p.put(str,p.getOrDefault(str,0) + 1);
        }
        
        for (String str : participant) {
            if(p.getOrDefault(str,0) == 0) {
                return str;
            } 
            
            p.put(str,p.getOrDefault(str,0) - 1);
        }
        
        return null;
    }
}