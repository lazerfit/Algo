import java.util.*;
class Solution {
    static List<String> a;
    static String[][] Tickets;
    static boolean[] visited;
    static List<String> route;
    
    static void dfs(int depth, String start) {
        if (depth == Tickets.length) {
            if (a == null) {
                a = new ArrayList<>(route);
            } else {
                for (int i =0;i<a.size();i++) {
                    if (!a.get(i).equals(route.get(i))) {
                        if (a.get(i).compareTo(route.get(i)) > 0) {
                            a = new ArrayList<>(route);    
                        }
                        break;
                    }
                }   
            }
        }
                
        for (int i=0;i<Tickets.length;i++) {
            if (!visited[i] && start.equals(Tickets[i][0])) {
                visited[i] = true;
                route.add(Tickets[i][1]);
                dfs(depth + 1, Tickets[i][1]);
                visited[i] = false;
                route.remove(route.size() - 1);
            }
        }
    }
    
    
    public String[] solution(String[][] tickets) {
        visited = new boolean[tickets.length];
        Tickets = tickets;
        a = null;
        route = new ArrayList<>();
        route.add("ICN");
        
        dfs(0, "ICN");
        
        
        return a.toArray(new String[0]);
    }
}