import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		Map<String, Double> score = Map.ofEntries(
			Map.entry("A+", 4.3), Map.entry("A0", 4.0), Map.entry("A-", 3.7),
			Map.entry("B+", 3.3), Map.entry("B0", 3.0), Map.entry("B-", 2.7),
			Map.entry("C+", 2.3), Map.entry("C0", 2.0), Map.entry("C-", 1.7),
			Map.entry("D+", 1.3), Map.entry("D0", 1.0), Map.entry("D-", 0.7),
			Map.entry("F", 0.0)
		);

		System.out.println(score.get(br.readLine()));
	}
}