import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[][] map;
	static int n;
	static int m;
	static long answer = 256 * 500 * 500;
	static int answerHeight;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());

		map = new int[n][m];
		int maxHeight = 0;

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				int input = Integer.parseInt(st.nextToken());

				if (input > maxHeight) {
					maxHeight = input;
				}

				map[i][j] = input;
			}
		}

		for (int h = 0; h <= maxHeight; h++) {
			cal(b, h);
		}

		System.out.println(answer + " " + answerHeight);
	}

	private static void cal(int remain, int h) {
		int removeCount = 0; // 깎아내서 인벤토리에 들어올 블록 수
		int addCount = 0;    // 채워 넣느라 소모될 블록 수

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				int diff = map[i][j] - h;

				if (diff > 0) {
					removeCount += diff; // 목표 높이보다 높으면 깎아냄
				} else if (diff < 0) {
					addCount -= diff;    // 목표 높이보다 낮으면 채워 넣음 (diff가 음수이므로 빼서 양수로 만듦)
				}
			}
		}

		// 전체 작업 후 인벤토리가 감당 가능한지 한 번에 확인
		if (remain + removeCount < addCount) {
			return;
		}

		int time = (removeCount * 2) + addCount;

		// 시간이 덜 걸리거나, 시간이 같은데 높이가 더 높은 경우 정답 갱신
		if (time < answer) {
			answer = time;
			answerHeight = h;
		} else if (time == answer && h > answerHeight) {
			answer = time;
			answerHeight = h;
		}
	}
}