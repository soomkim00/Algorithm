import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int[] dice = new int[3];

		for (int i = 0; i < 3; i++) {
			dice[i] = Integer.parseInt(st.nextToken());
		}

		Arrays.sort(dice);

		int sameCount = 1;
		int sameNumber = 0;

		for (int i = 1; i < 3; i++) {
			if (dice[i] == dice[i - 1]) {
				sameCount++;
				sameNumber = dice[i];
			}
		}

		if (sameCount == 3) {
			System.out.println(10000 + sameNumber * 1000);
		} else if (sameCount == 2) {
			System.out.println(1000 + sameNumber * 100);
		} else {
			System.out.println(100 * dice[2]);
		}
	}
}