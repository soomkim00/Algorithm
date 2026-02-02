import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		if (n == 0) {
			System.out.println(0);
			return;
		}

		int[] counts = new int[31];

		for (int i = 0; i < n; i++) {
			int input = Integer.parseInt(br.readLine());
			counts[input]++;
		}

		int temp = (int)Math.round(n * 0.15);
		int cnt = 0;

		for (int i = 1; i < 31; i++) {
			while (counts[i] > 0 && cnt < temp) {
				counts[i]--;
				cnt++;
			}
		}
		cnt = 0;

		for (int i = 30; i > 0; i--) {
			while (counts[i] > 0 && cnt < temp) {
				counts[i]--;
				cnt++;
			}
		}

		long total = 0;
		for (int i = 1; i < 31; i++) {
			total += (long)i * counts[i];
		}

		System.out.println(Math.round((double)total / (n - 2 * temp)));

	}
}