import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        String[] strings = new String[numbers.length];
        for (int i=0;i<numbers.length;i++) {
            strings[i] = String.valueOf(numbers[i]);
        }
        
        Arrays.sort(strings, (o1,o2) -> o2.repeat(3).compareTo(o1.repeat(3)));
        
        StringBuilder sb = new StringBuilder();
        
        for (String s : strings) {
            sb.append(s);
        }
        
        return sb.charAt(0) == '0' ? "0" : sb.toString();
    }
}