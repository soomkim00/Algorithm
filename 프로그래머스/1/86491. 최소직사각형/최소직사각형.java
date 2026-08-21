import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int maxW = 0;
        int maxH = 0;
        
        for (int[] row : sizes) {
            Arrays.sort(row);
            if (row[0] > maxW) {
                maxW = row[0];
            }
            if (row[1] > maxH) {
                maxH = row[1];
            }
        }
        
        return maxW * maxH;
    }
}