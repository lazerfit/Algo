import java.util.*;
import java.util.stream.Stream;
import java.util.stream.Collectors;
class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        HashMap<String, Set<String>> reportMap = new HashMap<>();
        HashMap<String, Integer> totalCount = new HashMap<>();
        HashMap<String, Integer> uid = new HashMap<>();
        
        for (int i=0;i<id_list.length;i++) {
            uid.put(id_list[i],i);
        }
        
        for (String s:report) {
            String[] cmd = s.split(" ");
            Set<String> reportedUser = reportMap.getOrDefault(cmd[0], new HashSet<String>());
            reportedUser.add(cmd[1]);
            reportMap.put(cmd[0], reportedUser);
        }
        
        reportMap.entrySet()
            .forEach(entry -> entry.getValue().forEach(v -> totalCount.put(v, totalCount.getOrDefault(v,0)+1)));
        
        Map<String, Integer> filteredCount = totalCount.entrySet().stream().filter(entry -> entry.getValue() >= k)
            .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
        
        reportMap.entrySet().forEach(entry -> 
                                     entry.getValue().forEach(v -> {
                                         if(filteredCount.containsKey(v)) {
                                             answer[uid.get(entry.getKey())] += 1;
                                             }
                                         }));

        return answer;
    }
}