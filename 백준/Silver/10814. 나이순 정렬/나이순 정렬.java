import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		String[][] members = new String[n][2];

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());

			String age = st.nextToken();
			String name = st.nextToken();

			members[i][0] = age;
			members[i][1] = name;
		}

		Arrays.sort(members, (m1, m2) -> {
			return Integer.parseInt(m1[0]) - Integer.parseInt(m2[0]);
		});

		for (int i = 0; i < n; i++) {
			System.out.println(members[i][0] + " " + members[i][1]);
		}
	}
}