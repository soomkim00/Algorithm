class Solution {
    public int solution(String binomial) {
        String[] arr = binomial.split(" ");
        
        int a = Integer.parseInt(arr[0]);
        int b = Integer.parseInt(arr[2]);
        
        if (arr[1].equals("+")) {
            return a + b;
        } else if (arr[1].equals("-")) {
            return a - b;
        } else {
            return a * b;
        }
    }
}