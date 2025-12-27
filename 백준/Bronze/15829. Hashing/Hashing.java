import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int l = Integer.parseInt(br.readLine());
		String input = br.readLine();

		final long M = 1234567891L;
		long hash = 0;
		long pow = 1; // 31^0

		for (int i = 0; i < input.length(); i++) {
			long val = input.charAt(i) - 'a' + 1; // a=1 ... z=26
			hash = (hash + val * pow) % M;
			pow = (pow * 31) % M; // 다음은 31^(i+1)
		}

		System.out.println(hash);
	}
}