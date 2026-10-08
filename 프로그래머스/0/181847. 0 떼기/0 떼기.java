class Solution {
    public String solution(String n_str) {
        StringBuilder sb = new StringBuilder();
        boolean flag = true;
        for (char c : n_str.toCharArray()) {
            if (flag && c == '0') {
                continue;
            } else {
                sb.append(c);
                flag = false;
            }
        }
        return sb.toString();
    }
}