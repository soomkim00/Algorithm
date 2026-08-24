import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        Arrays.fill(answer, -1);
        char[] arr = s.toCharArray();
        
        for (int i = 1; i < s.length(); i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (arr[i] == arr[j]) {
                    answer[i] = i - j;
                    break;
                }
            }
        }
        return answer;
    }
}