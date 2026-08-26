import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        int n = num_list.length;
        int[] answer = Arrays.copyOf(num_list, n + 1);

        int last = num_list[n - 1];
        int secondLast = num_list[n - 2];

        if (last > secondLast) {
            answer[n] = last - secondLast;
        } else {
            answer[n] = last * 2;
        }

        return answer;
    }
}