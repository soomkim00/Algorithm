import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[][] data = new int[9][9];
		int maxVal = 0;

		int r = 1;
		int c = 1;

		for (int i = 0; i < 9; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 9; j++) {
				int input = Integer.parseInt(st.nextToken());

				if (input > maxVal) {
					maxVal = input;
					r = i + 1;
					c = j + 1;
				}
			}
		}

		StringBuilder sb = new StringBuilder();
		sb.append(maxVal).append('\n').append(r).append(" ").append(c);
		System.out.print(sb);
	}
}