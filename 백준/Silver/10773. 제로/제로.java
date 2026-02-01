import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int k = Integer.parseInt(br.readLine());

		ArrayDeque<Long> stack = new ArrayDeque<>();
		for (int i = 0; i < k; i++) {
			long input = Long.parseLong(br.readLine());
			if (input == 0) {
				stack.pop();
			} else {
				stack.push(input);
			}
		}

		long result = 0;
		while (!stack.isEmpty()) {
			result += stack.pop();
		}
		System.out.print(result);
	}
}