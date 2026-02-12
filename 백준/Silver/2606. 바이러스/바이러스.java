import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int node = Integer.parseInt(br.readLine());
		int n = Integer.parseInt(br.readLine());

		ArrayList<Integer>[] graph = new ArrayList[node + 1];  // 1 ~ node

		for (int i = 0; i < node + 1; i++) {
			graph[i] = new ArrayList<>();
		}

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n1 = Integer.parseInt(st.nextToken());
			int n2 = Integer.parseInt(st.nextToken());

			graph[n1].add(n2);
			graph[n2].add(n1);  //양방향(무방향) 그래프
		}

		// bfs
		boolean[] visited = new boolean[node + 1];  // 1 ~ node
		ArrayDeque<Integer> queue = new ArrayDeque<>();
		queue.offer(1);
		visited[1] = true;
		int count = 0;

		while (!queue.isEmpty()) {
			int now = queue.poll();

			for (int next : graph[now]) {
				if (!visited[next]) {
					visited[next] = true;
					queue.offer(next);
					count++;
				}
			}
		}

		System.out.println(count);

	}
}