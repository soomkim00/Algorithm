import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		long[] data = new long[n];
		StringTokenizer st = new StringTokenizer(br.readLine());

		for (int i = 0; i < n; i++) {
			data[i] = Long.parseLong(st.nextToken());
		}

		Arrays.sort(data);

		int m = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();

		StringTokenizer st2 = new StringTokenizer(br.readLine());
		for (int i = 0; i < m; i++) {
			if (Arrays.binarySearch(data, Long.parseLong(st2.nextToken())) < 0) {
				sb.append(0).append('\n');
			} else {
				sb.append(1).append('\n');
			}
		}

		System.out.println(sb);
	}
}