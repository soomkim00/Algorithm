import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
       Map<String, Integer> hm = new HashMap<>();
       Map<String, List<int[]>> musicMap = new HashMap<>();

       for (int i = 0; i < plays.length; i++) {
          hm.put(genres[i], hm.getOrDefault(genres[i], 0) + plays[i]);
          
          musicMap.putIfAbsent(genres[i], new ArrayList<>());
          musicMap.get(genres[i]).add(new int[]{i, plays[i]});
       }

       List<Map.Entry<String, Integer>> entryList = new ArrayList<>(hm.entrySet());
       entryList.sort((o1, o2) -> o2.getValue().compareTo(o1.getValue()));
       
       List<Integer> answerList = new ArrayList<>();

       for (Map.Entry<String, Integer> entry : entryList) {
           String genre = entry.getKey();
           List<int[]> songs = musicMap.get(genre);

           songs.sort((o1, o2) -> {
               if (o1[1] == o2[1]) {
                   return Integer.compare(o1[0], o2[0]);
               }
               return Integer.compare(o2[1], o1[1]);
           });

           answerList.add(songs.get(0)[0]);
           if (songs.size() > 1) {
               answerList.add(songs.get(1)[0]);
           }
       }

       return answerList.stream().mapToInt(i -> i).toArray();
    }
}