import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String input = br.readLine();
		int n = Integer.parseInt(input);

		int start = n - input.length() * 9;
		int answer = 0;

		for (int i = Math.max(1, start); i <= n; i++) {
			if (getSum(i) == n) {
				answer = i;
				break;
			}
		}

		System.out.println(answer);

	}

	public static int getSum(int i) {
		int res = i;
		while (i > 0) {
			res += i % 10;
			i /= 10;
		}
		return res;
	}

}