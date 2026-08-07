class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for (int i = left; i <= right; i++) {
            if (cal(i) % 2 == 0) answer += i;
            else answer -= i; 
        }
        return answer;
    }
    
    private static int cal(int num) {
        int count = 1;
        for (int j = 2; j <= num; j++) {
            if (num % j == 0) count++;
        }
        return count;
    }
}