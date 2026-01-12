import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static class Member {
		int age;
		String name;

		public Member(int age, String name) {
			this.age = age;
			this.name = name;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		Member[] members = new Member[n];

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());

			int age = Integer.parseInt(st.nextToken());
			String name = st.nextToken();

			members[i] = new Member(age, name);
		}

		Arrays.sort(members, (m1, m2) -> {
			return m1.age - m2.age;
		});

		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < n; i++) {
			sb.append(members[i].age).append(" ").append(members[i].name).append('\n');
		}

		System.out.print(sb);
	}
}