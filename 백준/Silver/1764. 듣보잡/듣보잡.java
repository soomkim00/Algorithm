import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		Map<String, Integer> nameMap = new HashMap<>();

		for (int i = 0; i < n; i++) {
			String name = br.readLine();
			nameMap.put(name, 1);
		}

		int total = 0;
		ArrayList<String> list = new ArrayList<>();
		for (int i = 0; i < m; i++) {
			String name = br.readLine();
			if (nameMap.containsKey(name)) {
				total++;
				list.add(name);
			}
		}

		StringBuilder sb = new StringBuilder();
		Collections.sort(list);
		sb.append(total).append('\n');

		for (String name : list) {
			sb.append(name).append('\n');
		}

		System.out.print(sb);
	}
}