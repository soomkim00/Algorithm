import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		int[] times = new int[n];
		StringTokenizer st = new StringTokenizer(br.readLine());

		for (int i = 0; i < n; i++) {
			times[i] = Integer.parseInt(st.nextToken());
		}

		Arrays.sort(times);

		int total = times[0];
		for (int i = 1; i < n; i++) {
			times[i] += times[i - 1];
			total += times[i];
		}

		System.out.println(total);
	}
}