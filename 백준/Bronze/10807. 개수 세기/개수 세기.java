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
			int input = Integer.parseInt(st.nextToken());
			data[i] = input;
		}

		int v = Integer.parseInt(br.readLine());
		int result = 0;

		for (int j = 0; j < n; j++) {
			if (data[j] == v) {
				result++;
			}
		}

		System.out.println(result);
	}
}