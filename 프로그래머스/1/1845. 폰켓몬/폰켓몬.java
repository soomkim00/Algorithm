import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(int[] nums) {
        int size = nums.length;
        Set<Integer> hs = new HashSet<>();
        
        for (int num: nums) {
            hs.add(num);
        }
        
        int answer = hs.size() > size / 2 ? size / 2 : hs.size();
        return answer;
    }
}