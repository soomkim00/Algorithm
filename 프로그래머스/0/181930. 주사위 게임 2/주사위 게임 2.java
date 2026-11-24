class Solution {
    public int solution(int a, int b, int c) {
        int answer = a + b + c;
        if (a != b && b != c && c != a) {
            return answer;
        }
        
        answer *= (a * a + b * b + c * c);
        
        if (a == b && b == c && c == a) {
            answer *= (a * a * a + b * b * b + c * c * c);
        }
        
        return answer;
    }
}