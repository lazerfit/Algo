import java.util.*;
import java.util.stream.Stream;
class Solution {
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();
        HashMap<String, List<int[]>> genreMap = new HashMap<>(); 
        HashMap<String, Integer> playMap = new HashMap<>();
        
        for (int i = 0;i < genres.length; i++) {
            List<int[]> uid = genreMap.getOrDefault(genres[i], new ArrayList<int[]>());
            uid.add(new int[]{i, plays[i]});
            genreMap.put(genres[i], uid);
            playMap.put(genres[i], playMap.getOrDefault(genres[i],0) + plays[i]);
        }
        
        Stream<Map.Entry<String, Integer>> sortedGenre = playMap.entrySet().stream().sorted((o1,o2) -> Integer.compare(o2.getValue(), o1.getValue()));
        
        sortedGenre.forEach(entry -> {
            Stream<int[]> sortedSongs = genreMap.get(entry.getKey()).stream().sorted((o1,o2) -> Integer.compare(o2[1], o1[1])).limit(2);
            sortedSongs.forEach(song -> answer.add(song[0]));
        });
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}