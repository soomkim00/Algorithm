class Solution {
    public int[] solution(int[] array) {
        int max_num = 0;
        int idx = 0;
        for (int i = 0; i < array.length; i++) {
            if (array[i] > max_num) {
                max_num = array[i];
                idx = i;
            }
        }
        return new int[] {max_num, idx};
    }
}