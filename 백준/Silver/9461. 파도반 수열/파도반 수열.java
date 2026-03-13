import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());

		long[] data = new long[101];

		data[1] = 1;
		data[2] = 1;
		data[3] = 1;
		data[4] = 2;
		data[5] = 2;

		for (int i = 6; i <= 100; i++) {
			data[i] = data[i - 1] + data[i - 5];
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < t; i++) {
			int input = Integer.parseInt(br.readLine());
			sb.append(data[input]).append('\n');
		}

		System.out.print(sb);
	}
}