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
				if (input == 1) {
					map[r][c] = -1;
				} else if (input == 2) {
					sr = r;
					sc = c;
					map[r][c] = 0;
				} else {
					map[r][c] = input;
				}
			}
		}

		int[] dr = {-1, 1, 0, 0};
		int[] dc = {0, 0, -1, 1};

		ArrayDeque<int[]> queue = new ArrayDeque<>();  // (r, c, 길이)
		queue.offer(new int[] {sr, sc});

		while (!queue.isEmpty()) {
			int[] temp = queue.poll();
			int tr = temp[0];
			int tc = temp[1];

			for (int i = 0; i < 4; i++) {
				int nr = tr + dr[i];
				int nc = tc + dc[i];

				if (nr >= 0 && nr < n && nc >= 0 && nc < m && map[nr][nc] == -1) {
					map[nr][nc] = map[tr][tc] + 1;
					queue.offer(new int[] {nr, nc});
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