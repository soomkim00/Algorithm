import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[][] meeting = new int[n][2];

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());

			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());

			meeting[i][0] = s;
			meeting[i][1] = e;
		}

		Arrays.sort(meeting, (o1, o2) -> {
			if (o1[1] == o2[1]) {
				return Integer.compare(o1[0], o2[0]);
			}
			return Integer.compare(o1[1], o2[1]);
		});

		int temp = 0;  // 회의 끝 타임
		int count = 0;

		for (int[] meet : meeting) {
			int start = meet[0];
			int end = meet[1];

			if (start >= temp) {
				count++;
				temp = end;
			}
		}

		System.out.println(count);
	}
}