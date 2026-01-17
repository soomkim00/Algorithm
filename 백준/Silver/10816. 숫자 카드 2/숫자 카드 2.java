import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {

		int[] pos = new int[10000001];  // 0 ~ 10,000,000
		int[] neg = new int[10000001];  // -1 ~ -10,000,000

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());

		for (int i = 0; i < n; i++) {
			int input = Integer.parseInt(st.nextToken());
			if (input >= 0) {
				pos[input]++;
			} else {
				neg[-input]++;
			}
		}

		int m = Integer.parseInt(br.readLine());
		StringTokenizer st2 = new StringTokenizer(br.readLine());

		StringBuilder sb = new StringBuilder();

		for (int j = 0; j < m; j++) {
			int number = Integer.parseInt(st2.nextToken());
			if (number >= 0) {
				sb.append(pos[number]).append(" ");
			} else {
				sb.append(neg[-number]).append(" ");
			}
		}

		System.out.println(sb);
	}
}