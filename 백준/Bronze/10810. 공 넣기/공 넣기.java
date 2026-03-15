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

		int[] backet = new int[n + 1];

		for (int a = 0; a < m; a++) {
			StringTokenizer st2 = new StringTokenizer(br.readLine());

			int i = Integer.parseInt(st2.nextToken());
			int j = Integer.parseInt(st2.nextToken());
			int k = Integer.parseInt(st2.nextToken());

			for (int idx = i; idx <= j; idx++) {
				backet[idx] = k;
			}
		}

		StringBuilder sb = new StringBuilder();

		for (int i = 1; i <= n; i++) {
			sb.append(backet[i]).append(" ");
		}
		System.out.print(sb);
	}
}