import java.util.*;
class Solution {
    static List<String> list;
    static void makeList(int n, String now) {
        if (n == 5) {
            return;
        }
        list.add(now);
        makeList(n + 1, now + "A");
        makeList(n + 1, now + "E");
        makeList(n + 1, now + "I");
        makeList(n + 1, now + "O");
        makeList(n + 1, now + "U");  
    }
    
    public int solution(String word) {
        list = new ArrayList<>();
        
        makeList(0, "A");
        makeList(0, "E");
        makeList(0, "I");
        makeList(0, "O");
        makeList(0, "U");
        
        
        
        return list.indexOf(word) + 1;
    }
}