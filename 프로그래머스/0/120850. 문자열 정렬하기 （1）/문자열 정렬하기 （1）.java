import java.util.*;

class Solution {
    public int[] solution(String my_string) {
        ArrayList<Integer> list = new ArrayList<>();
        for (char c : my_string.toCharArray()) {
            if (Character.isDigit(c)) {
                list.add(c - '0');
            }
        }
        int[] answer = list.stream().mapToInt(i -> i).toArray();
        Arrays.sort(answer);
        return answer;
    }
}