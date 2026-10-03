class Solution {
    public int solution(int num, int k) {
        String numS = String.valueOf(num);
        char[] arr = numS.toCharArray();

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] - '0' == k) {
                return i + 1;
            }
        }
        return -1;
    }
}