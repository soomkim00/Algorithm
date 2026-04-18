import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
	static int n;
	static int[][] data;
	static int[][] delta = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static ArrayList<Integer> result;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());

		data = new int[n][n];

		for (int r = 0; r < n; r++) {
			String input = br.readLine();
			for (int c = 0; c < n; c++) {
				data[r][c] = input.charAt(c) - '0';
			}
		}

		int count = 0;
		result = new ArrayList<>();

		for (int r = 0; r < n; r++) {
			for (int c = 0; c < n; c++) {
				if (data[r][c] == 1) {
					count++;
					bfs(r, c);
				}
			}
		}

		Collections.sort(result);
		StringBuilder sb = new StringBuilder();
		sb.append(count).append('\n');
		for (int r : result) {
			sb.append(r).append('\n');
		}

		System.out.print(sb);
	}

	private static void bfs(int sr, int sc) {
		ArrayDeque<int[]> queue = new ArrayDeque<>();
		queue.offer(new int[] {sr, sc});
		data[sr][sc] = 0;
		int total = 1;

		while (!queue.isEmpty()) {
			int[] temp = queue.poll();
			int tr = temp[0];
			int tc = temp[1];

			for (int[] del : delta) {
				int nr = tr + del[0];
				int nc = tc + del[1];

				if (0 <= nr && nr < n && 0 <= nc && nc < n && data[nr][nc] == 1) {
					total++;
					data[nr][nc] = 0;
					queue.offer(new int[] {nr, nc});
				}
			}
		}
		result.add(total);
	}
}