import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int t = Integer.parseInt(br.readLine());

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < t; i++) {
			int n = Integer.parseInt(br.readLine());

			if (n == 0) {
				sb.append(0).append('\n');
				continue;
			}
			Map<String, Integer> map = new HashMap<>();

			for (int j = 0; j < n; j++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				String cloth = st.nextToken();
				String category = st.nextToken();

				map.put(category, map.getOrDefault(category, 0) + 1);
			}

			int result = 1;
			for (Integer value : map.values()) {
				result *= value + 1;
			}

			sb.append(result - 1).append('\n');
		}

		System.out.println(sb);
	}
}