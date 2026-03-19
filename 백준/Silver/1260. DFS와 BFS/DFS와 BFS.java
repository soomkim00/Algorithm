import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static boolean[] visited;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int v = Integer.parseInt(st.nextToken());

		ArrayList<Integer>[] adj = new ArrayList[n + 1];

		for (int i = 0; i <= n; i++) {
			adj[i] = new ArrayList<>();
		}

		for (int i = 0; i < m; i++) {
			StringTokenizer st2 = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st2.nextToken());
			int e = Integer.parseInt(st2.nextToken());

			adj[s].add(e);
			adj[e].add(s);
		}

		for (int i = 0; i <= n; i++) {
			Collections.sort(adj[i]);
		}

		visited = new boolean[n + 1];
		dfs(adj, v);
		sb.append('\n');

		visited = new boolean[n + 1];
		bfs(adj, n, v);

		System.out.println(sb);
	}

	private static void dfs(ArrayList<Integer>[] adj, int now) {
		visited[now] = true;
		sb.append(now).append(" ");

		for (int next : adj[now]) {
			if (!visited[next]) {
				dfs(adj, next);
			}
		}

	}

	private static void bfs(ArrayList<Integer>[] adj, int n, int v) {
		Deque<Integer> queue = new ArrayDeque<>();
		queue.offer(v);
		visited[v] = true;

		while (!queue.isEmpty()) {
			int now = queue.poll();
			sb.append(now).append(" ");

			for (int next : adj[now]) {
				if (!visited[next]) {
					visited[next] = true;
					queue.offer(next);
				}
			}
		}
	}
}