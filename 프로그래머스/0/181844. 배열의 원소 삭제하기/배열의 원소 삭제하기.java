import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        ArrayList<Integer> list = new ArrayList<>();

        for (int num : arr) {
            boolean flag = true;
            for (int delNum : delete_list) {
                if (num == delNum) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                list.add(num);
            }
        }
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}