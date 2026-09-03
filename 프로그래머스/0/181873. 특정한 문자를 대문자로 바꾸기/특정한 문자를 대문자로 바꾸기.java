class Solution {
    public String solution(String my_string, String alp) {
        StringBuilder sb = new StringBuilder();
        for (char ch : my_string.toCharArray()) {
            sb.append(ch == alp.charAt(0) ? Character.toUpperCase(ch) : ch);
        }
        return sb.toString();
    }
}