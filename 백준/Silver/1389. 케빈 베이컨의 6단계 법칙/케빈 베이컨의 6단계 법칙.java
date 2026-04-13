import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static ArrayList<Integer>[] adj;
	static int[][] dist;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		adj = new ArrayList[n + 1];

		for (int i = 1; i <= n; i++) {
			adj[i] = new ArrayList<>();
		}

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());

			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			adj[a].add(b);
			adj[b].add(a);
		}

		dist = new int[n + 1][n + 1];

		for (int i = 1; i <= n; i++) {
			bfs(i);
		}

		int[] total = new int[n + 1];

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				total[i] += dist[i][j];
			}
		}

		int minIdx = 0;
		int minVal = 10000;

		for (int i = 1; i <= n; i++) {
			if (total[i] < minVal) {
				minIdx = i;
				minVal = total[i];
			}
		}

		System.out.println(minIdx);
	}

	private static void bfs(int node) {
		boolean[] visited = new boolean[n + 1];
		ArrayDeque<int[]> queue = new ArrayDeque<>();

		queue.offer(new int[] {node, 0});
		visited[node] = true;

		while (!queue.isEmpty()) {
			int[] now = queue.poll();
			int nowNode = now[0];
			int nowCount = now[1];

			for (int next : adj[nowNode]) {
				if (!visited[next]) {
					visited[next] = true;

					dist[node][next] = nowCount + 1;
					dist[next][node] = nowCount + 1;

					queue.offer(new int[] {next, nowCount + 1});
				}
			}
		}
	}
}