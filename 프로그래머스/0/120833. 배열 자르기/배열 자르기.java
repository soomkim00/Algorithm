class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        int count = num2 - num1 + 1;
        int[] answer = new int[count];
        int idx = num1;
        for (int i = 0; i < count; i++) {
            answer[i] = numbers[idx];
            idx++;
        }
        return answer;
    }
}