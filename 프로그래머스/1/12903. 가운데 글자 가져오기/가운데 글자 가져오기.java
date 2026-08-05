class Solution {
    public String solution(String s) {
        int len = s.length();
        char[] arr = s.toCharArray();
        if (len % 2 == 1) {
            return arr[len / 2] + "";
        } 
        else {
            return "" + arr[len / 2 - 1] + arr[len / 2];
        }
    }
}