class Solution {
    public int solution(int num) {
        int answer = 0;
        long numl = num;
        while (numl != 1 && answer <= 500) {
            if (numl % 2 == 0) numl /= 2;
            else numl = numl * 3 + 1;
            answer++;
        }
        
        return answer == 501 ? -1 : answer;
    }
}