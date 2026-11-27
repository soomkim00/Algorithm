class Solution {
    public int[] solution(int[] numbers, String direction) {
        int len = numbers.length;
        int[] answer = new int[len];
        int i = direction.equals("right") ? len - 1 : 1;
        
        for (int j = 0; j < len; j++) {
            answer[j] = numbers[i % len];
            i++;
        }
        
        return answer;
    }
}