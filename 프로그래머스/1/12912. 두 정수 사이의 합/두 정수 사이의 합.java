class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        if (a == b) return a;
        int s = a;
        int e = b;
        if (a > b) {
            s = b;
            e = a;
        }
        for (int i = s; i <= e; i++) {
            answer += i;
        }
        return answer;
    }
}