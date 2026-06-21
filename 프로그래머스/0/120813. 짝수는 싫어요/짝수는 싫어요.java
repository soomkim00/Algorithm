import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int n) {
        int[] answer = new int[(int) Math.ceil(n / 2.0)];
        int idx = 0;
        
        for (int i = 1; i <= n; i += 2) {
            answer[idx] = i;
            idx++;
        }
        
        return answer;
    }
}