class Solution {
    public int solution(String myString, String pat) {
        StringBuilder sb = new StringBuilder();
        for (char c : pat.toCharArray()) {
            sb.append(c == 'A' ? 'B' : 'A');
        }
        return myString.contains(sb.toString()) ? 1 : 0;
    }
}