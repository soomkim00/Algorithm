import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());

		int[] result = new int[12];  // 0 ~ 11
		for (int i = 0; i < 12; i++) {
			result[i] = solve(i);
		}

		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < t; i++) {
			int input = Integer.parseInt(br.readLine());
			sb.append(result[input]).append('\n');
		}

		System.out.print(sb);
	}

	public static int solve(int target) {
		return dfs(0, target);
	}

	private static int dfs(int currentSum, int target) {
		if (currentSum > target) {
			return 0;
		}

		if (currentSum == target) {
			return 1;
		}

		return dfs(currentSum + 1, target)
			+ dfs(currentSum + 2, target)
			+ dfs(currentSum + 3, target);
	}
}