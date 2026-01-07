import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		// 완탐
		int count = 1;
		int num = 666; // 첫 수부터 시작 (n >= 1)

		while (count < n) {
			num++;

			String temp = String.valueOf(num);
			if (temp.contains("666")) {
				count++;
			}
		}

		System.out.println(num);
	}
}