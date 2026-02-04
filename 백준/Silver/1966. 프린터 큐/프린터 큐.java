import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());

		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < t; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());

			int[] count = new int[10];  // 중요도 count, 0 ~ 9
			ArrayDeque<Integer[]> queue = new ArrayDeque<>();  // [idx, 중요도] 담을 queue

			// 중요도 입력
			StringTokenizer st2 = new StringTokenizer(br.readLine());
			for (int idx = 0; idx < n; idx++) {
				int score = Integer.parseInt(st2.nextToken());
				queue.add(new Integer[] {idx, score});

				// 중요도 count
				count[score]++;
			}

			int order = 1;  // 출력 순서
			while (!queue.isEmpty()) {
				Integer[] front = queue.poll();  // 맨 앞 문서

				//  현재 최고 중요도 계산
				int highScore = 1;
				for (int j = 9; j > 0; j--) {
					if (count[j] > 0) {
						highScore = j;
						break;
					}
				}

				if (front[1] != highScore) {  // 중요도가 가장 높지 않으면 뒤로
					queue.add(front);
				} else if (front[0] == m) {  // 찾는 문서인지 확인
					sb.append(order).append('\n');
					break;
				} else {  // 아니면 출력 후 다음 문서로
					order++;
					count[highScore]--;
				}
			}
		}

		System.out.print(sb);
	}
}