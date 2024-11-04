import java.util.*;
class Solution {
    public int[] solution(String s) {

        s = s.substring(0,s.length() - 2).replace("{","");
        String[] temp = s.split("},");
        Arrays.sort(temp, (o1,o2) -> Integer.compare(o1.length(), o2.length()));
        
        HashSet<String> set = new HashSet<>();
        int[] answer = new int[temp.length];
        
        for (int i=0;i<temp.length;i++) {
            String[] numbers = temp[i].split(",");
            for (String number : numbers) {
                if(!set.contains(number)) {
                    answer[i] = Integer.parseInt(number);
                    set.add(number);
                }
            }
        }
        
        
        return answer;
    }
}