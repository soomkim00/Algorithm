import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static int result = 64;
	public static char[][] board;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		board = new char[n][m];

		for (int i = 0; i < n; i++) {
			String input = br.readLine();
			for (int j = 0; j < m; j++) {
				board[i][j] = input.charAt(j);
			}
		}

		// // board의 시작 칸 설정
		for (int i = 0; i < n - 7; i++) {
			for (int j = 0; j < m - 7; j++) {
				check(i, j);
			}
		}

		System.out.println(result);

	}

	public static void check(int x, int y) {
		int countB = 0;  // 시작점 B 일 때 바꿔야 할 칸 개수
		int flag = (x + y) % 2;  //시작 칸의 좌표 합이 홀/짝인지

		for (int i = x; i < x + 8; i++) {
			for (int j = y; j < y + 8; j++) {
				if (((i + j) % 2 == flag && board[i][j] == 'W') || ((i + j) % 2 != flag && board[i][j] == 'B')) {
					countB++;
				}
			}
		}

		int countMin = Math.min(countB, 64 - countB);

		result = Math.min(result, countMin);
	}

}