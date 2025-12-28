import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());

		int[][] arr = new int[15][14];

		// 0층: 1,2,3,...,14
		for (int i = 0; i < 14; i++) {
			arr[0][i] = i + 1;
		}

		// 나머지 층 채우기
		// arr[k][n] = (n == 0) ? 1 : arr[k][n-1] + arr[k-1][n]
		for (int k = 1; k < 15; k++) {
			for (int n = 0; n < 14; n++) {
				if (n == 0) arr[k][n] = 1;
				else arr[k][n] = arr[k][n - 1] + arr[k - 1][n];
			}
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < t; i++) {
			int k = Integer.parseInt(br.readLine());
			int n = Integer.parseInt(br.readLine()); // 1~14

			sb.append(arr[k][n - 1]).append('\n'); // n-1로 인덱싱
		}

		System.out.print(sb);
	}
}
