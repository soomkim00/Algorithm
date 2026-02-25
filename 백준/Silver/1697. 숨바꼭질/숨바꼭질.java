import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());

		if (n == k) {
			System.out.println(0);
			return;
		}

		int[] dist = new int[100001];
		Arrays.fill(dist, -1);  // -1이면 미방문
		ArrayDeque<Integer> queue = new ArrayDeque<>();  // pos

		queue.offer(n);
		dist[n] = 0;  // 방문 처리

		while (!queue.isEmpty()) {
			int pos = queue.poll();

			for (int nextPos : new int[] {pos + 1, pos - 1, pos * 2}) {
				if (nextPos >= 0 && nextPos <= 100000 && dist[nextPos] == -1) {
					if (nextPos == k) {
						System.out.println(dist[pos] + 1);
						return;
					}

					dist[nextPos] = dist[pos] + 1;
					queue.offer(nextPos);
				}
			}
		}
	}
}