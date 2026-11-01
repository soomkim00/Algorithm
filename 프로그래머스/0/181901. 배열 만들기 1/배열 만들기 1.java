class Solution {
    public int[] solution(int n, int k) {
        int[] answer = new int[n / k];
        int i = 0;
        for (int num = 1; num <= n; num++) {
            if (num % k == 0) {
                answer[i] = num;
                i++;
            }
        }
        return answer;
    }
}