import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		int[] rawData = new int[n];
		StringTokenizer st = new StringTokenizer(br.readLine());

		for (int i = 0; i < n; i++) {
			rawData[i] = Integer.parseInt(st.nextToken());
		}

		int[] sortedData = rawData.clone();
		Arrays.sort(sortedData);

		HashMap<Integer, Integer> rankingMap = new HashMap<>(n);
		int rank = 0;

		for (int value : sortedData) {
			if (!rankingMap.containsKey(value)) {
				rankingMap.put(value, rank);
				rank++;
			}
		}

		StringBuilder sb = new StringBuilder();

		for (int value : rawData) {
			sb.append(rankingMap.get(value)).append(' ');
		}
		System.out.print(sb);
	}
}