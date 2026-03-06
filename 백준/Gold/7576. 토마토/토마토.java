import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int m = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());

		int[][] box = new int[n][m];
		int count = 0;
		ArrayDeque<int[]> queue = new ArrayDeque<>();

		for (int i = 0; i < n; i++) {
			StringTokenizer st2 = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				int input = Integer.parseInt(st2.nextToken());
				box[i][j] = input;

				if (input == 0) {
					count++;
				} else if (input == 1) {
					queue.offer(new int[] {i, j, 0});
				}
			}
		}

		int[] dr = new int[] {-1, 1, 0, 0};
		int[] dc = new int[] {0, 0, -1, 1};

		int lastDay = 0;

		while (!queue.isEmpty()) {
			int[] temp = queue.poll();

			for (int i = 0; i < 4; i++) {
				int nr = temp[0] + dr[i];
				int nc = temp[1] + dc[i];

				if (nr >= 0 && nr < n && nc >= 0 && nc < m && box[nr][nc] == 0) {
					box[nr][nc] = 1;
					count--;
					lastDay = temp[2] + 1;
					queue.offer(new int[] {nr, nc, temp[2] + 1});
				}
			}
		}

		if (count == 0) {
			System.out.println(lastDay);
		} else {
			System.out.println(-1);
		}
	}
}