import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] arr = new int[10001];

		for (int i = 0; i < n; i++) {
			int num = Integer.parseInt(br.readLine());
			arr[num]++;
		}

		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		for (int j = 0; j < 10001; j++) {
			if (arr[j] != 0) {
				for (int k = 0; k < arr[j]; k++) {
					bw.write(String.valueOf(j));
					bw.newLine();
				}
			}
		}
		bw.flush();
		bw.close();

	}
}