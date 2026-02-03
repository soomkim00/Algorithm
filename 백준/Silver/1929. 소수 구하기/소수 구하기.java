import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int m = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());

		boolean[] check = new boolean[n + 1];  // 0 ~ n
		check[1] = true;  // 1은 소수가 아니다

		for (int i = 2; i <= n; i++) {
			if (!check[i]) {
				int mul = 2;
				while (i * mul <= n) {
					check[i * mul] = true;
					mul++;
				}
			}
		}

		StringBuilder sb = new StringBuilder();
		for (int i = m; i <= n; i++) {
			if (!check[i]) {
				sb.append(i).append('\n');
			}
		}

		System.out.print(sb);
	}
}