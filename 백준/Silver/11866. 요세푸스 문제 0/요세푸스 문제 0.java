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
		int k = Integer.parseInt(st.nextToken());

		Deque<Integer> queue = new ArrayDeque<>();

		for (int i = 1; i <= n; i++) {
			queue.offer(i);
		}

		StringBuilder sb = new StringBuilder();
		sb.append("<");

		for (int i = 0; i < n - 1; i++) {
			for (int j = 0; j < k - 1; j++) {
				queue.offer(queue.poll());
			}

			sb.append(queue.poll()).append(", ");
		}

		sb.append(queue.poll()).append(">");
		System.out.print(sb);

	}
}