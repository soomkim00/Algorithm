import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		int[][] data = new int[n][2];

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			data[i][0] = Integer.parseInt(st.nextToken());
			data[i][1] = Integer.parseInt(st.nextToken());
		}

		Arrays.sort(data, (d1, d2) -> {
			return d1[1] == d2[1] ? Integer.compare(d1[0], d2[0]) : Integer.compare(d1[1], d2[1]);
		});

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < n; i++) {
			sb.append(data[i][0]).append(" ").append(data[i][1]).append('\n');
		}

		System.out.print(sb);
	}
}