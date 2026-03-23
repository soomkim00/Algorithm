import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] data = new int[] {1, 1, 2, 2, 2, 8};

		StringBuilder sb = new StringBuilder();

		StringTokenizer st = new StringTokenizer(br.readLine());

		for (int i = 0; i < 6; i++) {
			int input = Integer.parseInt(st.nextToken());
			sb.append(data[i] - input).append(" ");
		}

		System.out.println(sb);
	}
}