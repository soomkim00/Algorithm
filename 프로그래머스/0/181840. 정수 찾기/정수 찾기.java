class Solution {
    public int solution(int[] num_list, int n) {
        for (int temp : num_list) {
            if (temp == n) return 1;
        }
        return 0;
    }
}