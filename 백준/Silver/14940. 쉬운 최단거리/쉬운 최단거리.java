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
		int sr = 0;
		int sc = 0;

		for (int r = 0; r < n; r++) {
			StringTokenizer st2 = new StringTokenizer(br.readLine());
			for (int c = 0; c < m; c++) {
				int input = Integer.parseInt(st2.nextToken());
				map[r][c] = input;
				if (input == 2) {
					sr = r;
					sc = c;
					map[r][c] = 0;
				}
			}
		}

		int[] dr = {-1, 1, 0, 0};
		int[] dc = {0, 0, -1, 1};
		boolean[][] visited = new boolean[n][m];

		ArrayDeque<int[]> queue = new ArrayDeque<>();  // (r, c, 길이)
		queue.offer(new int[] {sr, sc, 0});
		visited[sr][sc] = true;

		while (!queue.isEmpty()) {
			int[] temp = queue.poll();
			int tr = temp[0];
			int tc = temp[1];
			int dist = temp[2];

			for (int i = 0; i < 4; i++) {
				int nr = tr + dr[i];
				int nc = tc + dc[i];

				if (nr >= 0 && nr < n && nc >= 0 && nc < m && map[nr][nc] != 0 && !visited[nr][nc]) {
					map[nr][nc] = dist + 1;
					visited[nr][nc] = true;
					queue.offer(new int[] {nr, nc, dist + 1});
				}
			}
		}

		for (int r = 0; r < n; r++) {
			for (int c = 0; c < m; c++) {
				if (map[r][c] == 1 && !visited[r][c]) {
					map[r][c] = -1;
				}
			}
		}

		StringBuilder sb = new StringBuilder();
		for (int r = 0; r < n; r++) {
			for (int c = 0; c < m; c++) {
				sb.append(map[r][c]).append(' ');
			}
			sb.append('\n');
		}

		System.out.print(sb);
	}
}