class Solution {
	public String solution(String my_string, int n) {
		StringBuilder answer = new StringBuilder();
		for (char ch : my_string.toCharArray()) {
			for (int i = 0; i < n; i++) {
                answer.append(ch);
            }
		}
		return answer.toString();
	}
}