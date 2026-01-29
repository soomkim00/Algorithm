import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Main {
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		while (true) {
			String input = br.readLine();
			if (input.equals("."))
				break;

			solve(input);
		}
		System.out.print(sb);
	}

	public static void solve(String text) {
		ArrayDeque<Character> stack = new ArrayDeque<>();
		for (char c : text.toCharArray()) {
			if (c == '(' || c == '[') {
				stack.push(c);
			} else if (c == ')') {
				if (stack.isEmpty() || stack.peek() == '[') {
					sb.append("no").append('\n');
					return;
				} else {
					stack.pop();
				}
			} else if (c == ']') {
				if (stack.isEmpty() || stack.peek() == '(') {
					sb.append("no").append('\n');
					return;
				} else {
					stack.pop();
				}
			}
		}
		if (stack.isEmpty()) {
			sb.append("yes").append('\n');
		} else {
			sb.append("no").append('\n');
		}
	}
}