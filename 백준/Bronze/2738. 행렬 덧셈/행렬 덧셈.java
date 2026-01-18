import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st1 = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st1.nextToken());
		int m = Integer.parseInt(st1.nextToken());

		int[][] result = new int[n][m];

		for (int idx = 0; idx < 2; idx++) {
			for (int i = 0; i < n; i++) {
				StringTokenizer st2 = new StringTokenizer(br.readLine());

				for (int j = 0; j < m; j++) {
					result[i][j] += Integer.parseInt(st2.nextToken());
				}
			}
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				sb.append(result[i][j]).append(" ");
			}
			sb.append('\n');
		}

		System.out.println(sb);
	}
}