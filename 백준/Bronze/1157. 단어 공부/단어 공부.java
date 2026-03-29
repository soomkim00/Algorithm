import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String input = br.readLine();
		input = input.toUpperCase();

		int[] counts = new int[26];

		for (char c : input.toCharArray()) {
			counts[c - 'A']++;
		}

		int pos = 0;
		int maxVal = 0;
		boolean flag = false;

		for (int i = 0; i < 26; i++) {
			if (counts[i] > maxVal) {
				pos = i;
				maxVal = counts[i];
				flag = false;
			} else if (counts[i] == maxVal) {
				flag = true;
			}
		}

		if (flag) {
			System.out.println('?');
		} else {
			System.out.println((char)(pos + 'A'));
		}
	}
}