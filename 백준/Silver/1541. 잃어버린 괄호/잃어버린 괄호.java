import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String input = br.readLine();

		StringBuilder temp = new StringBuilder();
		int result = 0;
		boolean isMinus = false;

		for (char c : input.toCharArray()) {
			if (Character.isDigit(c)) {
				temp.append(c);
			} else {
				int number = Integer.parseInt(temp.toString());
				temp.setLength(0);

				if (isMinus) {
					result -= number;
				} else {
					result += number;
				}

				if (c == '-') {
					isMinus = true;
				}
			}
		}

		int number = Integer.parseInt(temp.toString());

		if (isMinus) {
			result -= number;
		} else {
			result += number;
		}

		System.out.println(result);
	}
}