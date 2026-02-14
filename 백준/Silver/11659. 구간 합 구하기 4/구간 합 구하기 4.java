import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		int[] numbers = new int[n + 1];
		StringTokenizer st2 = new StringTokenizer(br.readLine());
		for (int i = 1; i <= n; i++) {
			numbers[i] = Integer.parseInt(st2.nextToken());
		}

		for (int i = 2; i <= n; i++) {
			numbers[i] += numbers[i - 1];
		}

		StringBuilder sb = new StringBuilder();
		for (int k = 0; k < m; k++) {
			StringTokenizer st3 = new StringTokenizer(br.readLine());
			int i = Integer.parseInt(st3.nextToken());
			int j = Integer.parseInt(st3.nextToken());

			sb.append(numbers[j] - numbers[i - 1]).append('\n');
		}

		System.out.print(sb);
	}
}