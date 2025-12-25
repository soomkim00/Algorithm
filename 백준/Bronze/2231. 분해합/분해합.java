import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		for (int i = 1; i <= n; i++) {
			int result = i;
			int add_num = i;

			while (add_num != 0) {
				result += add_num % 10;
				add_num /= 10;
			}

			if (result == n) {
				System.out.println(i);
				return;
			}

		}
		System.out.println(0);
		
	}

}