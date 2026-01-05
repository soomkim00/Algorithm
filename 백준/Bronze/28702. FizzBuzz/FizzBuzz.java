import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int nextNumber = 0;

		for (int i = 0; i < 3; i++) {
			String input = br.readLine();

			char firstChar = input.charAt(0);

			if (Character.isDigit(firstChar)) {
				int number = Integer.parseInt(input);
				nextNumber = number + (3 - i);
			}
		}

		if (nextNumber % 3 == 0 && nextNumber % 5 == 0) {
			System.out.println("FizzBuzz");
		} else if (nextNumber % 3 == 0) {
			System.out.println("Fizz");
		} else if (nextNumber % 5 == 0) {
			System.out.println("Buzz");
		} else {
			System.out.println(nextNumber);
		}
	}
}