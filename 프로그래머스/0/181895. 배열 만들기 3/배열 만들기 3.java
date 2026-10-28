class Solution {
    public int[] solution(int[] arr, int[][] intervals) {
        int len1 = intervals[0][1] - intervals[0][0] + 1;
        int len2 = intervals[1][1] - intervals[1][0] + 1;
        int[] answer = new int[len1 + len2];
        
        int idx = intervals[0][0];
        for (int i = 0; i < len1; i++) {
            answer[i] = arr[idx];
            idx++;
        }
        
        idx = intervals[1][0];
        for (int i = len1; i < answer.length; i++) {
            answer[i] = arr[idx];
            idx++;
        }
        
        return answer;
    }
}