import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int m;
	static int[] tree;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		tree = new int[n];
		int maxHeight = 0;

		StringTokenizer st2 = new StringTokenizer(br.readLine());

		for (int i = 0; i < n; i++) {
			tree[i] = Integer.parseInt(st2.nextToken());
			if (tree[i] > maxHeight) {
				maxHeight = tree[i];
			}
		}

		System.out.println(solve(maxHeight));
	}

	private static int solve(int maxHeight) {
		int left = 0;
		int right = maxHeight;

		while (left <= right) {
			int mid = left + (right - left) / 2;

			if (isEnough(mid)) {
				left = mid + 1;
			} else {
				right = mid - 1;
			}
		}

		return right;
	}

	private static boolean isEnough(int height) {
		long total = 0;

		for (int i = 0; i < tree.length; i++) {
			if (tree[i] > height) {
				total += tree[i] - height;
				if (total >= m) {
					return true;
				}
			}
		}
		return false;
	}
}