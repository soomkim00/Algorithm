class Solution {
    public int solution(int price) {
        int result = (int) Math.floor(price >= 500000 ? price * 0.80 : price >= 300000 ? price * 0.9 : price >= 100000 ? price * 0.95 : price) ;
        return result;
    }
}