import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		char[][] data = new char[5][15];
		for (int i = 0; i < 5; i++) {
			String input = br.readLine();
			for (int j = 0; j < input.length(); j++) {
				data[i][j] = input.charAt(j);
			}
		}

		StringBuilder sb = new StringBuilder();
		for (int j = 0; j < 15; j++) {
			for (int i = 0; i < 5; i++) {
				if (data[i][j] != '\u0000') {
					sb.append(data[i][j]);
				}
			}
		}

		System.out.println(sb);
	}
}