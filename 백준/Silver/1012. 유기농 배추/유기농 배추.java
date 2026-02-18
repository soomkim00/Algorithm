import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());

		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < t; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int m = Integer.parseInt(st.nextToken());
			int n = Integer.parseInt(st.nextToken());
			int k = Integer.parseInt(st.nextToken());

			boolean[][] board = new boolean[n][m];

			for (int j = 0; j < k; j++) {
				StringTokenizer st2 = new StringTokenizer(br.readLine());
				int c = Integer.parseInt(st2.nextToken());
				int r = Integer.parseInt(st2.nextToken());

				board[r][c] = true;
			}

			int count = 0;

			for (int tr = 0; tr < n; tr++) {
				for (int tc = 0; tc < m; tc++) {
					if (board[tr][tc]) {
						count++;
						bfs(tr, tc, n, m, board);
					}
				}
			}

			sb.append(count).append('\n');
		}

		System.out.print(sb);
	}

	static int[][] delta = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

	private static void bfs(int r, int c, int n, int m, boolean[][] board) {
		Deque<int[]> queue = new ArrayDeque<>();
		queue.offer(new int[] {r, c});
		board[r][c] = false;

		while (!queue.isEmpty()) {
			int[] current = queue.poll();
			int tr = current[0];
			int tc = current[1];

			for (int[] dir : delta) {
				int nr = tr + dir[0];
				int nc = tc + dir[1];

				if (isRange(nr, nc, n, m) && board[nr][nc]) {
					board[nr][nc] = false;
					queue.offer(new int[] {nr, nc});
				}
			}
		}
	}

	private static boolean isRange(int r, int c, int n, int m) {
		return r >= 0 && r < n && c >= 0 && c < m;
	}
}