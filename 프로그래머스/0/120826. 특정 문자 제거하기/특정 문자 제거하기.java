class Solution {
    public String solution(String my_string, String letter) {
        StringBuilder sb = new StringBuilder();
        
        for (char ch : my_string.toCharArray()) {
            if (ch != letter.charAt(0)) {
                sb.append(ch);
            }
        }
        return sb.toString();
    }
}