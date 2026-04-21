import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		int m = Integer.parseInt(br.readLine());
		char[] input = br.readLine().toCharArray();

		int left = 0;
		int right = 0;
		int result = 0;
		int count = 0;

		for (int i = 0; i < m; i++) {
			if (input[i] == 'I') {
				left = i;
				right = i;
				break;
			}
		}

		while (right < m - 2) {
			if (input[right + 1] != 'O') {
				count = 0;
				right++;
				left = right;
			} else if (input[right + 2] != 'I') {
				count = 0;
				while (right < m - 2) {
					right++;
					if (input[right] == 'I') {
						left = right;
						break;
					}
				}
			} else {
				count++;
				right += 2;
				if (count == n) {
					result++;
					count = 0;
					left += 2;
					right = left;
				}
			}
		}

		System.out.println(result);
	}
}