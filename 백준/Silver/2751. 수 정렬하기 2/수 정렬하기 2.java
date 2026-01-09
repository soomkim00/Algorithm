import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		boolean[] pos = new boolean[1000001];
		boolean[] neg = new boolean[1000001];

		for (int i = 0; i < n; i++) {
			int input = Integer.parseInt(br.readLine());

			if (input >= 0) {
				pos[input] = true;
			} else {
				neg[-input] = true;
			}
		}

		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for (int j = 1000000; j > 0; j--) {
			if (neg[j]) {
				bw.write("-" + j + "\n");
			}
		}

		for (int k = 0; k <= 1000000; k++) {
			if (pos[k]) {
				bw.write(k + "\n");
			}
		}

		bw.flush();
		bw.close();
		br.close();
	}
}