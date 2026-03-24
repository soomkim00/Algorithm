import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[] line;
	static int k;
	static int n;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		k = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());

		line = new int[k];
		long max = 0; // 입력받은 랜선 중 가장 긴 길이를 저장

		for (int i = 0; i < k; i++) {
			line[i] = Integer.parseInt(br.readLine());
			if (max < line[i]) {
				max = line[i]; // 최댓값 갱신
			}
		}

		// 탐색 범위는 1부터 가장 긴 랜선의 길이까지
		solve(1, max);
	}

	private static void solve(long left, long right) { // long 타입 사용
		long mid = 0;

		while (left <= right) {
			mid = (left + right) / 2;

			long total = 0; // 만들어진 랜선의 총 개수
			for (int i = 0; i < k; i++) {
				total += (line[i] / mid);
			}

			// 조건 판별 (매개변수 탐색의 Upper Bound 방식)
			if (total >= n) {
				// n개 이상 만들 수 있다면, 길이를 더 늘려본다 (최대 길이를 찾기 위함)
				left = mid + 1;
			} else {
				// n개를 만들 수 없다면, 길이를 줄여야 한다
				right = mid - 1;
			}
		}

		// Upper Bound 방식으로 최댓값을 찾을 때는 while문 종료 후 right가 정답이 됩니다.
		System.out.println(right);
	}
}