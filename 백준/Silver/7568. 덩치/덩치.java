import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		int[][] students = new int[n][2];  // x, y

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());

			students[i][0] = x;
			students[i][1] = y;
		}

		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		for (int idx = 0; idx < n; idx++) {
			int rank = 1;
			for (int j = 0; j < n; j++) {
				if (idx == j) {
					continue;
				} else {
					if (students[idx][0] < students[j][0] && students[idx][1] < students[j][1]) {
						rank++;
					}
				}
			}
			bw.write(rank + " ");
		}

		bw.flush();
		bw.close();
		br.close();
	}
}