class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        long pNum = Long.parseLong(p);
        int pLen = p.length();
        
        for (int i = 0; i <= t.length() - pLen; i++) {
            if (Long.parseLong(t.substring(i, i + pLen)) <= pNum) {
                answer++;
            }
        }
        return answer;
    }
}