import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		int[] data = new int[n];
		StringTokenizer st = new StringTokenizer(br.readLine());

		for (int i = 0; i < n; i++) {
			data[i] = Integer.parseInt(st.nextToken());
		}

		int[] count = new int[10];
		int left = 0;
		int kind = 0;
		int result = 0;

		for (int right = 0; right < n; right++) {
			if (count[data[right]] == 0) {
				kind++;
			}
			count[data[right]]++;

			while (kind > 2) {
				count[data[left]]--;
				if (count[data[left]] == 0) {
					kind--;
				}
				left++;
			}

			result = Math.max(result, right - left + 1);
		}

		System.out.println(result);
	}
}