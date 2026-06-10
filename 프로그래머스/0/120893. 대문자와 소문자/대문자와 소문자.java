class Solution {
    public String solution(String my_string) {
        StringBuilder answer = new StringBuilder();
        for (char ch : my_string.toCharArray()) {
            if (Character.isUpperCase(ch)) answer.append(Character.toLowerCase(ch));
            else answer.append(Character.toUpperCase(ch));
        }
        return answer.toString();
    }
}