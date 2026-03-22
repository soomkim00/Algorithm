import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		int[] baskets = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			baskets[i] = i;
		}

		for (int k = 0; k < M; k++) {
			st = new StringTokenizer(br.readLine());
			int left = Integer.parseInt(st.nextToken());
			int right = Integer.parseInt(st.nextToken());

			while (left < right) {
				int temp = baskets[left];
				baskets[left] = baskets[right];
				baskets[right] = temp;
				left++;
				right--;
			}
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 1; i <= N; i++) {
			sb.append(baskets[i]).append(" ");
		}
		System.out.println(sb.toString().trim());
	}
}