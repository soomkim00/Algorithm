import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		int[][] map = new int[n][m];

		for (int i = 0; i < n; i++) {
			String input = br.readLine();
			for (int j = 0; j < m; j++) {
				map[i][j] = input.charAt(j) - '0';
			}
		}

		ArrayDeque<int[]> queue = new ArrayDeque<>();
		queue.offer(new int[] {0, 0, 1});  // r, c, map[r][c]
		map[0][0] = 0;

		int[][] delta = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

		while (!queue.isEmpty()) {
			int[] temp = queue.poll();
			int tr = temp[0];
			int tc = temp[1];
			int td = temp[2];

			for (int[] del : delta) {
				int nr = tr + del[0];
				int nc = tc + del[1];

				if (0 <= nr && nr < n && 0 <= nc && nc < m && map[nr][nc] == 1) {
					if (nr == n - 1 && nc == m - 1) {
						System.out.println(td + 1);
						return;
					}

					map[nr][nc] = td + 1;
					queue.offer(new int[] {nr, nc, td + 1});
				}
			}
		}
	}
}