import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());

		long[] fibo0 = new long[41];
		long[] fibo1 = new long[41];

		fibo0[0] = 1;
		fibo0[1] = 0;
		fibo1[0] = 0;
		fibo1[1] = 1;

		for (int i = 2; i <= 40; i++) {
			fibo0[i] = fibo0[i - 1] + fibo0[i - 2];
			fibo1[i] = fibo1[i - 1] + fibo1[i - 2];
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < t; i++) {
			int input = Integer.parseInt(br.readLine());
			sb.append(fibo0[input]).append(" ").append(fibo1[input]).append('\n');
		}

		System.out.print(sb);
	}
}