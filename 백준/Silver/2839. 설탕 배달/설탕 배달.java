import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		if (n % 5 == 0) {
			System.out.println(n / 5);
			return;
		} else {
			int remain = n % 5;
			int count = n / 5;

			while (remain <= n) {
				if (remain % 3 == 0) {
					System.out.println(count + remain / 3);
					return;
				}

				remain += 5;
				count--;
			}
		}
		System.out.println(-1);

	}
}