import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int i = 1;

		while (true) {
			if (n == 1) {
				System.out.println(1);
				break;
			}

			if (n <= (1 + 6 * makeSum(i))) {
				System.out.println(i + 1);
				break;
			} else {
				i++;
			}
		}

	}

	public static int makeSum(int i) {
		int result = 0;

		for (int j = 0; j <= i; j++) {
			result += j;
		}

		return result;
	}

}