class Solution {
	public int[] solution(long n) {
		String nStr = n + "";
		int len = nStr.length();
		int[] answer = new int[len];
		int idx = len-1;
		for (char c : nStr.toCharArray()) {
			answer[idx] = c - 48;
			idx--;
		}
		return answer;
	}
}