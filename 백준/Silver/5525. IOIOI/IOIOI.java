import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		int m = Integer.parseInt(br.readLine());
		char[] input = br.readLine().toCharArray();

		int result = 0;
		int count = 0;

		for (int i = 0; i < m-2; i++) {
			if (input[i] == 'I' && input[i+1] == 'O' && input[i+2] == 'I') {
				count++;
				if (count == n) {
					result++;
					count--;
				}
				i++;
			} else {
				count = 0;
			}
		}

		System.out.println(result);
	}
}