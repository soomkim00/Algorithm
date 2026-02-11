import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		int[] memo = new int[n + 1];

		Arrays.fill(memo, 1000000);

		memo[1] = 0;

		for (int i = 1; i <= n; i++) {
			int current = memo[i];

			if (i + 1 <= n) {
				memo[i + 1] = Math.min(current + 1, memo[i + 1]);
			}
			if (i * 2 <= n) {
				memo[i * 2] = Math.min(current + 1, memo[i * 2]);
			}
			if (i * 3 <= n) {
				memo[i * 3] = Math.min(current + 1, memo[i * 3]);
			}
		}
		System.out.println(memo[n]);
	}
}