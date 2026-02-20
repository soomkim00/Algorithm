import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[] result = new int[2];
	static int[][] paper;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		paper = new int[n][n];

		for (int r = 0; r < n; r++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int c = 0; c < n; c++) {
				paper[r][c] = Integer.parseInt(st.nextToken());
			}
		}

		checkColor(0, 0, n);

		System.out.println(result[0]);
		System.out.println(result[1]);

	}

	private static void checkColor(int sr, int sc, int size) {
		int color = paper[sr][sc];  // 맨 위의 색상

		for (int r = sr; r < sr + size; r++) {
			for (int c = sc; c < sc + size; c++) {
				if (paper[r][c] != color) {
					int newSize = size / 2;

					checkColor(sr, sc, newSize);  // 1사분면
					checkColor(sr, sc + newSize, newSize);  // 2사분면
					checkColor(sr + newSize, sc, newSize);  // 3사분면
					checkColor(sr + newSize, sc + newSize, newSize); // 4사분면
					return;
				}
			}
		}

		result[color]++;
	}
}