import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		int[] step = new int[n + 1];

		for (int i = 1; i <= n; i++) {
			step[i] = Integer.parseInt(br.readLine());
		}

		if (n == 1) {
			System.out.println(step[1]);
			return;
		} else if (n == 2) {
			System.out.println(step[1] + step[2]);
			return;
		}

		int[] dp = new int[n + 1];

		dp[1] = step[1];
		dp[2] = dp[1] + step[2];
		dp[3] = Math.max(dp[1], dp[0] + step[2]) + step[3];

		for (int i = 4; i <= n; i++) {
			dp[i] = Math.max(dp[i - 2], dp[i - 3] + step[i - 1]) + step[i];
		}

		System.out.println(dp[n]);
	}
}