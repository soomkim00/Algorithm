import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		char[][] campus = new char[n][m];
		int sr = 0;
		int sc = 0;

		for (int i = 0; i < n; i++) {
			String input = br.readLine();
			for (int j = 0; j < m; j++) {
				char c = input.charAt(j);
				if (c == 'I') {
					sr = i;
					sc = j;
				}
				campus[i][j] = c;
			}
		}

		int result = 0;

		Deque<int[]> queue = new ArrayDeque<>();
		queue.offer(new int[] {sr, sc});

		int[][] delta = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

		while (!queue.isEmpty()) {
			int[] temp = queue.poll();
			int tr = temp[0];
			int tc = temp[1];

			for (int[] del : delta) {
				int nr = tr + del[0];
				int nc = tc + del[1];

				if (0 <= nr && nr < n && 0 <= nc && nc < m && campus[nr][nc] != 'X') {
					if (campus[nr][nc] == 'P')
						result++;

					campus[nr][nc] = 'X';
					queue.offer(new int[] {nr, nc});
				}
			}
		}

		if (result == 0) {
			System.out.println("TT");
		} else {
			System.out.println(result);
		}
	}
}