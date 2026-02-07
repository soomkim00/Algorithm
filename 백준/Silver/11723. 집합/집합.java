import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int m = Integer.parseInt(br.readLine());

		boolean[] set = new boolean[21];  // 0 ~ 20
		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < m; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String input = st.nextToken();
			switch (input) {
				case "add":
					int addNum = Integer.parseInt(st.nextToken());
					set[addNum] = true;
					break;
				case "remove":
					int removeNum = Integer.parseInt(st.nextToken());
					set[removeNum] = false;
					break;
				case "check":
					int checkNum = Integer.parseInt(st.nextToken());
					if (set[checkNum]) {
						sb.append(1).append('\n');
					} else {
						sb.append(0).append('\n');
					}
					break;
				case "toggle":
					int toggleNum = Integer.parseInt(st.nextToken());
					set[toggleNum] = !set[toggleNum];
					break;
				case "all":
					for (int j = 1; j <= 20; j++) {
						set[j] = true;
					}
					break;
				case "empty":
					for (int j = 1; j <= 20; j++) {
						set[j] = false;
					}
					break;
			}

		}
		System.out.print(sb);
	}
}