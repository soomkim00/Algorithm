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
		int k = Integer.parseInt(st.nextToken());

		if (n == k) {
			System.out.println(0);
			return;
		}

		boolean[] visited = new boolean[100001];
		ArrayDeque<int[]> queue = new ArrayDeque<>();  // pos, count

		queue.offer(new int[] {n, 0});
		visited[n] = true;

		while (!queue.isEmpty()) {
			int[] current = queue.poll();

			int pos = current[0];
			int count = current[1];

			for (int nextPos : new int[] {pos + 1, pos - 1, pos * 2}) {
				if (nextPos >= 0 && nextPos <= 100000 && !visited[nextPos]) {
					if (nextPos == k) {
						System.out.println(count + 1);
						return;
					}

					visited[nextPos] = true;
					queue.offer(new int[] {nextPos, count + 1});
				}
			}
		}
	}
}