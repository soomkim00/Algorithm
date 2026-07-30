class Solution {
    public String solution(String[] seoul) {
        int pos = 0;
        for (int i = 0; i < seoul.length; i++) {
            if (seoul[i].equals("Kim")) {
                pos = i;
                break;
            }
        }
        return "김서방은 " + pos + "에 있다";
    }
}