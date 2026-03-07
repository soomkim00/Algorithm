import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		String[] nameArray = new String[n];
		Map<String, Integer> nameMap = new HashMap<>();

		for (int i = 0; i < n; i++) {
			String input = br.readLine();
			nameArray[i] = input;
			nameMap.put(input, i);
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < m; i++) {
			String input = br.readLine();
			if (isNumeric(input)) {
				sb.append(nameArray[Integer.parseInt(input) - 1]).append('\n');
			} else {
				sb.append(nameMap.get(input) + 1).append('\n');
			}
		}

		System.out.print(sb);
	}

	private static boolean isNumeric(String s) {
		return Character.isDigit(s.charAt(0));
	}
}