class Solution {
    public String solution(String rsp) {
        String answer = "";
        for (char c : rsp.toCharArray()) {
            answer += c == '0' ? '5' : c == '2' ? '0' : '2';
        }
        return answer;
    }
}