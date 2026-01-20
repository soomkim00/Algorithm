import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
		int n = Integer.parseInt(br.readLine());

		ArrayDeque<Integer> queue = new ArrayDeque<>();
		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String command = st.nextToken();

			switch (command) {
				case "push":
					queue.offer(Integer.parseInt(st.nextToken()));
					break;
				case "pop":
					sb.append(queue.isEmpty() ? -1 : queue.poll()).append('\n');
					break;
				case "size":
					sb.append(queue.size()).append('\n');
					break;
				case "empty":
					sb.append(queue.isEmpty() ? 1 : 0).append('\n');
					break;
				case "front":
					sb.append(queue.isEmpty() ? -1 : queue.peek()).append('\n');
					break;
				case "back":
					sb.append(queue.isEmpty() ? -1 : queue.peekLast()).append('\n');
			}
		}

		System.out.println(sb);

	}
}