class Solution {
    public int[] solution(int[] num_list) {
        int odd_count = 0;
        int even_count = 0;
        for (int num : num_list) {
            if (num % 2 == 0) {
                even_count++;
            } else {
                odd_count++;
            }
        }
        return new int[] {even_count, odd_count};
    }
}