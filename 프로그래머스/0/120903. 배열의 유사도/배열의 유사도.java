import java.util.Arrays;

class Solution {
    public int solution(String[] s1, String[] s2) {
        Arrays.sort(s1);
        Arrays.sort(s2);
        
        int answer = 0;
        int idx2Start = 0;
        
        for (int idx1 = 0; idx1 < s1.length; idx1++) {
            for (int idx2 = idx2Start; idx2 < s2.length; idx2++) {
                if (s1[idx1].equals(s2[idx2])) {
                    answer++;
                    idx2Start = idx2 + 1;
                    break;
                }
            }
        }
        
        return answer;
    }
}