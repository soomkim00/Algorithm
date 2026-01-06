import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		List<List<String>> data = new ArrayList<>();

		for (int i = 0; i < 51; i++) {
			data.add(new ArrayList<>());
		}

		for (int j = 0; j < n; j++) {
			String input = br.readLine();
			data.get(input.length()).add(input);
		}

		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		for (int k = 0; k < 51; k++) {
			String temp = "";

			if (!data.get(k).isEmpty()) {
				List<String> words = data.get(k);
				Collections.sort(words);
				for (int l = 0; l < words.size(); l++) {
					String word = words.get(l);
					if (!word.equals(temp)) {
						temp = word;
						bw.write(word);
						bw.newLine();
					}
				}
			}
		}
		bw.flush();
		bw.close();
		br.close();
	}
}