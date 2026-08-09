class Solution {
    public long solution(int price, int money, int count) {
        long total = (long) price * ( (count * (count + 1) ) / 2);
        long answer = money - total;
        return answer >= 0 ? 0 : -answer;
    }
}