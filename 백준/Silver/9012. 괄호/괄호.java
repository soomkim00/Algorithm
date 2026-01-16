import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());

		for (int i = 0; i < t; i++) {
			String input = br.readLine();
			String result = "YES";

			Deque<Character> stack = new ArrayDeque<>();
			for (int j = 0; j < input.length(); j++) {
				char temp = input.charAt(j);
				if (temp == '(') {
					stack.push('(');
				} else {  // temp == ')'
					if (stack.isEmpty()) {
						result = "NO";
						break;
					} else {
						stack.pop();
					}
				}
			}

			if (!stack.isEmpty()) {
				result = "NO";
			}

			System.out.println(result);
		}
	}
}