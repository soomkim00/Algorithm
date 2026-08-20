class Solution {
    public int solution(int n) {
        StringBuilder sb = new StringBuilder();
        while (n >= 3) {
            sb.append(n % 3);
            n /= 3;
        }
        sb.append(n);
        
        int answer = 0;
        int len = sb.length();
        for (int i = 0; i < len; i++) {
            int num = sb.charAt(len - 1 - i) - '0';
            answer += Math.pow(3, i) * num;
        }
        return answer;
    }
    
}