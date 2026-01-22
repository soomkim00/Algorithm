import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());

		boolean[] numbers = new boolean[n];  // 0 ~ n-1 > 출력 시 +1
		int idx = 0;
		StringBuilder sb = new StringBuilder();
		sb.append("<");

		for (int i = 0; i < n; i++) {
			int temp = 0;

			while (true) {
				if (!numbers[idx]) {
					temp++;
				}
				if (temp == k) {
					numbers[idx] = true;
					break;
				}
				idx = idx == n - 1 ? 0 : idx + 1;
			}

			sb.append(idx + 1).append(", ");
		}
		sb.delete(sb.length() - 2, sb.length()).append(">");
		System.out.print(sb);

	}
}