class Solution {
	public String solution(String phone_number) {
		int len = phone_number.length();
		StringBuilder sb = new StringBuilder(len);

		int i = 0;
		for (;i < len - 4; i++) {
			sb.append('*');
		}

		for (;i < len; i++) {
			sb.append(phone_number.charAt(i));
		}

		return sb.toString();
	}
}