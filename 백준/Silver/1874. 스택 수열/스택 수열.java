import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		StringBuilder sb = new StringBuilder();
		ArrayDeque<Integer> stack = new ArrayDeque<>();
		int current = 1;

		for (int i = 0; i < n; i++) {
			int input = Integer.parseInt(br.readLine());

			while (current <= input) {
				stack.push(current++);
				sb.append("+").append('\n');
			}

			if (stack.peek() == input) {
				stack.pop();
				sb.append("-").append('\n');
			} else {
				System.out.println("NO");
				return;
			}
		}

		System.out.print(sb);
	}
}